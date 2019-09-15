from predictors.predictor import Predictor
import mechanize
from bs4 import BeautifulSoup
import re

br = mechanize.Browser()
#DONE
def calc_prediction(seq_len, text):
    result = ['-'] * seq_len
    intervals = re.findall(r"(\d+-\d+)", text)
    for i in intervals:
        [interval_begin, interval_end] = i.split('-')
        for c in range(int(interval_begin)-1, int(interval_end)):
            result[c] = 'D'
    #print(result)
    return result

class disembl(Predictor):
    def calculate(self):
        global br
        url = "http://dis.embl.de/"
        br.set_handle_robots(False)
        br.open(url)
        br.form = list(br.forms())[0]
        br['sequence_string'] = self.sequence 
        response = br.submit()
        #print(response.read())
        soup = BeautifulSoup(response.read(), features='html5lib')
        soup = soup.prettify()
        loops = re.findall(r"none_LOOPS\s+([-\d\s,]+)", soup)
        coils = re.findall(r"none_HOTLOOPS\s+([-\d\s,]+)", soup)
        rem465 = re.findall(r"none_REM465\s+([-\d\s,]+)", soup)
        seq_len = len(self.sequence)
        results_loops = calc_prediction(seq_len, loops[0])
        results_coils = calc_prediction(seq_len, coils[0])
        results_rem465 = calc_prediction(seq_len, rem465[0])
        results = [results_loops, results_coils, results_rem465]
        return results