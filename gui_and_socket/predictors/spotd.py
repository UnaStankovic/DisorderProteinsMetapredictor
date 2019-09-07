from predictors.predictor import Predictor
import mechanize
from bs4 import BeautifulSoup
import re
import requests, zipfile, io
import urllib

br = mechanize.Browser()

def open_link(soup, url):
    global br
    # As soon as the response is obtained, the link to the results should be followed
    link_url = re.findall("info/.*.htm", str(soup))
    new_url = url + str(link_url[0])
    response1 = br.open(new_url)
    print(response1.read())
    return response1 

class spotd(Predictor):
    def calculate(self):
        #self.calculated = [0, 2, 0.3, 1, 1, 0.7, 1]
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
        results = open_link(soup, url)
        
        #response1 = br.open(new_url)
        #soup = BeautifulSoup(response1.read(), features="html5lib")
        #print(response1.geturl())
        #print(response1.info())  # headers
        #print(response1.read()) # body
        #br.open(new_url)
        #soup = BeautifulSoup(response.read(), features='html5lib')
        #result_url = re.findall("info/SPOT-disorder/[0-9]+/spotd.tgz", str(soup))
        #print(result_url)
        #print("Opened second")
        #r = requests.get(result_url)
        
        #if(r.ok):
        #    z = zipfile.ZipFile(io.BytesIO(r.content))
        #   z.extractall()
        #    print("Unziped")
        #    print(z)
        return results
