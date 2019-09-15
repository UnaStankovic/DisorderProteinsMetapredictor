from sklearn import metrics as m 
import numpy as np
"""
def measure_individually(predictors, y):
    result = []
    for pred in predictors:
        result.append(measure_all(pred,y))
    return result
"""
def binarize_values(x):
    new = []
    for el in x:
        if el == "D":
            new.append(1)
        else:
            new.append(0)
    return new

def measure_all(x,y):
    a = round(m.accuracy_score(x,y),4)
    p = round(m.precision_score(x,y),4)
    f = round(m.f1_score(x,y),4)
    r = round(m.recall_score(x,y),4)
    return [a,p,r,f]