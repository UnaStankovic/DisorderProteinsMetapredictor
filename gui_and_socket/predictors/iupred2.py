from predictors.predictor import Predictor
import subprocess
import re 

#done - to fix sequence part 
class iupred2(Predictor):
    def calculate(self):
        filename = "sequence.txt"
        result = subprocess.check_output('python3 Predictors_codes/iupred2a/iupred2a.py ' + filename + ' long', shell=True)
        result = re.findall("[0-9]\t[A-Z]\t[0-9].[0-9]+", result.decode('ascii'))
        for r in result:
            pred = r[4:]
            if(float(pred) > 0.5):
                pred = "D"
            else:
                pred = "-"
            self.calculated.append(pred)
        return self.calculated
        
