from predictors.predictor import Predictor
import subprocess
import re 

#done - to fix sequence part 
class iupred2(Predictor):
    def calculate(self):
        filename = "sequence.txt"
        #retval = os.system('python3 ../Predictors_codes/iupred2a/iupred2a.py ' + filename + ' long')
        #if(retval == 0):
        result = subprocess.check_output('python3 Predictors_codes/iupred2a/iupred2a.py ' + filename + ' long', shell=True)
        result = re.findall("[0-9]\t[A-Z]\t[0-9].[0-9]+", result.decode('ascii'))
        aa = []
        for r in result:
            #a = r[2]
            pred = r[4:]
            #aa.append(a) # Just to be able to easily check if results are correct
            if(float(pred) > 0.5):
                pred = "D"
            else:
                pred = "-"
            self.calculated.append(pred)
        return self.calculated
        
