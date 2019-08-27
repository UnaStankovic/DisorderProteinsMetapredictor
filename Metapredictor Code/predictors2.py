#!/usr/bin/python
import re 
import os 
import subprocess
import mechanize

from bs4 import BeautifulSoup

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
def pondr(sequence, url):
    global br
    br.open(url)
    br.form = list(br.forms())[1] 
    br['ProteinName'] = "test"
    br['Sequence'] = sequence 
    response = br.submit()
    #print(response.read())
    soup = BeautifulSoup(response.read(), features='html5lib')
    print(soup.prettify())
    return soup

#DONE
#python3 iupred2a.py P53_HUMAN.seq long
# IUPred2A: context-dependent prediction of protein disorder as a function of redox state and protein binding
# Prediction type: long
# Prediction output
# POS   RES     IUPRED2
#1       M       0.9807
#2       E       0.9849
#3       E       0.9875
#4       P       0.9693
#python3 iupred2a.py P53_HUMAN.seq long
def iupred2():
    filename = "P53_HUMAN.seq"
    #retval = os.system('python3 ../Predictors/iupred2a/iupred2a.py ' + filename + ' long')
    #if(retval == 0):
    result = subprocess.check_output('python3 ../../Predictors/iupred2a/iupred2a.py ' + filename + ' long', shell=True)
    result = re.findall("[0-9]\t[A-Z]\t[0-9].[0-9]+", result.decode('ascii'))
    predicted = []
    aa = []
    for r in result:
      a = r[2]
      pred = r[4:]
      aa.append(a)
      predicted.append(pred)
    rez = (aa, predicted)
    #print(rez[0][0], rez[1][0])
    print(rez)
    return rez

#SPOTD fasta format
def spotd(sequence, url):
    global br
    br.open(url)
    br.form = list(br.forms())[0]
    br['SEQUENCE'] = sequence 
    response = br.submit()
    #print(response.read())
    soup = BeautifulSoup(response.read(), features='html5lib')
    print(soup.prettify())
    return soup

#ESPRITZ fasta format
def espritz(sequence, url):
    global br
    br.open(url)
    #br.form = list(br.forms())
    br.form = br.forms()[0]
    br['sequence'] = sequence
    br['model']= ["Disprot"]
    try:
        response = br.submit()
        soup = BeautifulSoup(response.read())
        print(soup)
    except mechanize._mechanize.HTTPError:
        pass
    
    print("HIII")

def cspritz(sequence, url):
    global br
    br.open(url)
    #br.form = list(br.forms())
    br.form = br.forms()[0]
    br['sequence'] = sequence
    #br['model']= ["Disprot"]
    try:
        response = br.submit()
        soup = BeautifulSoup(response.read())
        print(soup)
    except mechanize._mechanize.HTTPError:
        pass
    
    print("HIII")

def main():
    sequence_pondr = "MKTQRDGHSLGRWSLVLLLLGLVMPLAIIAQVLSYKEAVLRAIDGINQRSSDANLYRLLDLDPRPTMDGDPDTPKPVSFTVKETVCPRTTQQSPEDCDFKKDGLVKRCMGTVTLNQARGSFDISCDKDNKRFALLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES"
    sequence = ">sp|Q08209|PP2BA_HUMAN Serine/threonine-protein phosphatase 2B catalytic subunit alpha isoform OS=Homo sapiens OX=9606 GN=PPP3CA PE=1 SV=1MKTQRDGHSLGRWSLVLLLLGLVMPLAIIAQVLSYKEAVLRAIDGINQRSSDANLYRLLDLDPRPTMDGDPDTPKPVSFTVKETVCPRTTQQSPEDCDFKKDGLVKRCMGTVTLNQARGSFDISCDKDNKRFALLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES"
    br.set_handle_robots( False )
    br.set_handle_redirect(True)  
    br.addheaders = [('User-agent', 'Chrome')]

    #URLs
    URL_PONDR = "http://www.pondr.com/cgi-bin/pondr.cgi" 
    URL_SPOTD = "http://sparks-lab.org/server/SPOT-disorder/"
    URL_ESPRITZ = "http://protein.bio.unipd.it/espritz/"
    URL_CSPRITZ = "http://protein.bio.unipd.it/cspritz/"
    #pondr(sequence_pondr, URL_PONDR)
    iupred2()
    #spotd(sequence, URL_SPOTD)
    #espritz(sequence, URL_ESPRITZ)
    #cspritz(sequence, URL_CSPRITZ)

    #when all done adjust to multiple sequences
    #do output comparisons
if __name__ == "__main__":
    main()
