from predictors.predictor import Predictor
import subprocess
import re 

#done
class iupred2(Predictor):
    def calculate(self):
        filename = "P53_HUMAN.seq"
        #retval = os.system('python3 ../Predictors/iupred2a/iupred2a.py ' + filename + ' long')
        #if(retval == 0):
        result = subprocess.check_output('python3 ../../Predictors/iupred2a/iupred2a.py ' + filename + ' long', shell=True)
        result = re.findall("[0-9]\t[A-Z]\t[0-9].[0-9]+", result.decode('ascii'))
        aa = []
        for r in result:
            a = r[2]
            pred = r[4:]
            aa.append(a)
            self.calculated.append(pred)
        rez = (aa, self.calculated)
        #print(rez[0][0], rez[1][0])
        #print(rez)
        return rez
