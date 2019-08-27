from predictors.predictor import Predictor
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()

class spotd(Predictor):
    def calculate(self, sequence, url):
        #self.calculated = [0, 2, 0.3, 1, 1, 0.7, 1]
        global br
        br.open(url)
        br.form = list(br.forms())[0]
        br['SEQUENCE'] = sequence 
        response = br.submit()
        #print(response.read())
        soup = BeautifulSoup(response.read(), features='html5lib')
        print(soup.prettify())
        return soup
