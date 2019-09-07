from predictors.predictor import Predictor
from predictors.iupred2 import iupred2
from predictors.spotd import spotd
from predictors.pondr import pondr
#from predctors.espritz import espritz
#from predictors.cspritz import cspritz


def iupred2_predict(sequence):
    p = iupred2(sequence)
    return p.calculate()

def spotd_predict(sequence):
    p = spotd(sequence)
    return p.calculate()

def pondr_predict(sequence):
    p = pondr(sequence)
    return p.calculate()
"""
def cspritz_predict(sequence):
    p = cspritz(sequence)
    return p.calculate()

def espritz_predict(sequence):
    p = espritz(sequence)
    return p.calculate()
"""