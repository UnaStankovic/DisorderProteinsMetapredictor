from predictors.predictor import Predictor
import mechanize
from bs4 import BeautifulSoup
import re
import requests, zipfile, io
import urllib
import time
import threading

br = mechanize.Browser()
#DONE BUT WORKING VERY SLOW 
def parse_result(text):
    r = re.findall(r'SPOD:\s[0-9]+\s+(.*)\s+[0-9]+', text)
    result = []
    for elem in r:
        for c in elem:
            if (c in ['D','-']):
                result.append(c)
    print(result)
    print(len(result))
    return result

def open_link(soup, url):
    global br
    # As soon as the response is obtained, the link to the results should be followed
    link_url = re.findall("info/.*.htm", str(soup))
    new_url = url + str(link_url[0])
    #print(new_url)
    #s = requests.session()
    #s.config['keep_alive'] = False
    response1 = requests.get(new_url).text
    return response1 

class spotd(Predictor):
    def calculate(self):
        global br
        url = "http://sparks-lab.org/server/SPOT-disorder/"
        br.set_handle_robots(False)
        br.open(url)
        br.form = list(br.forms())[0]
        br['SEQUENCE'] = self.sequence 
        response = br.submit()
        #print(response.read())
        soup = BeautifulSoup(response.read(), features='html5lib')
        #print(soup.prettify())
        results = ''
        while True:
            results = open_link(soup, url)
            if 'Please wait' in results:
                time.sleep(10)
                print('Trying again...')
            else:
                break
        #print(results)
        self.calculated = parse_result(results)
        return self.calculated
        

