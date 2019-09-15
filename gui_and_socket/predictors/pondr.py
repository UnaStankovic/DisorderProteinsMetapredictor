from predictors.predictor import Predictor
import mechanize
from bs4 import BeautifulSoup
import re
from sock_serv import shortened_sequence

br = mechanize.Browser()
#CREATING A CONNECTION TO PREDICTOR, SUBMITTING THE SEQUENCE AND GETTING THE RESULT
"""===============================VLXT NNP STATISTICS================================
Predicted residues: 170                 Number Disordered Regions: 5
Number residues disordered: 69          Longest Disordered Region: 29
Overall percent disordered: 40.59       Average Prediction Score: 0.4130
Predicted disorder segment [1]-[9]      Average Strength= 0.8317
Predicted disorder segment [68]-[79]    Average Strength= 0.6641
Predicted disorder segment [88]-[99]    Average Strength= 0.5746
Predicted disorder segment [134]-[140]  Average Strength= 0.5516
Predicted disorder segment [142]-[170]  Average Strength= 0.7857
</pre>
  <pre>================================PREDICTOR OUTPUT================================
           "D" = Disordered                         " " = Ordered                
================================================================================
</pre>
  <pre>1         MKTQRDGHSL GRWSLVLLLL GLVMPLAIIA QVLSYKEAVL RAIDGINQRS
VLXT     DDDDDDDDD                                             


51       SDANLYRLLD LDPRPTMDGD PDTPKPVSFT VKETVCPRTT QQSPEDCDFK
VLXT                       DDD DDDDDDDDD         DDD DDDDDDDDD 


101      KDGLVKRCMG TVTLNQARGS FDISCDKDNK RFALLGDFFR KSKEKIGKEF
VLXT                                         DDDDDDD  DDDDDDDDD


151      KRIVQRIKDF LRNLVPRTES
VLXT     DDDDDDDDDD DDDDDDDDDD"""
#PONDR
class pondr(Predictor):
    def calculate(self):
      global br
      url = "http://www.pondr.com/cgi-bin/pondr.cgi" 
      br.set_handle_robots(False)
      br.open(url)
      br.form = list(br.forms())[1] 
      br['ProteinName'] = "test"
      br['Sequence'] = self.sequence 
      response = br.submit()
      soup = BeautifulSoup(response.read(), features='html5lib')
      soup = soup.prettify()
      result = re.findall("VLXT\t\s.*", soup)
      # We don't need a first one because it is not sequence
      result = result[1:]
      predicted = []
      for r in result:
          pred = r[6:]
          predicted.append(pred)
      total = []
      # Getting everything in one sequence 
      for i in predicted:
        total += i
      old = len(total)
      
      pom = shortened_sequence(self.sequence)
      if(old < len(self.sequence)):
        for i in range(0,len(pom) - old):
          total.append(" ")
      total = [x if x != ' ' else '-' for x in total ]
      
      self.calculated = total
      return self.calculated


