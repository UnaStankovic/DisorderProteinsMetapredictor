import sys
sys.path.append(".")

from predictors.iupred2 import iupred2
from predictors.spotd import spotd
from predictors.pondr import pondr
#from predctors.espritz import espritz
#from predictors.cspritz import cspritz

sequence = ">sp|Q08209|PP2BA_HUMAN Serine/threonine-protein phosphatase 2B catalytic subunit alpha isoform OS=Homo sapiens OX=9606 GN=PPP3CA PE=1 SV=1MKTQRDGHSLGRWSLVLLLLGLVMPLAIIAQVLSYKEAVLRAIDGINQRSSDANLYRLLDLDPRPTMDGDPDTPKPVSFTVKETVCPRTTQQSPEDCDFKKDGLVKRCMGTVTLNQARGSFDISCDKDNKRFALLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES"
sequence_pondr = "MKTQRDGHSLGRWSLVLLLLGLVMPLAIIAQVLSYKEAVLRAIDGINQRSSDANLYRLLDLDPRPTMDGDPDTPKPVSFTVKETVCPRTTQQSPEDCDFKKDGLVKRCMGTVTLNQARGSFDISCDKDNKRFALLGDFFRKSKEKIGKEFKRIVQRIKDFLRNLVPRTES"
iupred2_predictor = iupred2(sequence)
spotd_predictor = spotd(sequence)
pondr_predictor = pondr(sequence_pondr)
#espritz_predictor = espritz('asdsdsd')
# espritz_predictor = cspritz('asdsdsd')

predictors_list = [iupred2_predictor, spotd_predictor, pondr_predictor, spotd_predictor]

for p in predictors_list:
    p.calculate()
    print(p.get_all_values())
    print(p.get_weighted_value_for_AA(2,4))
    print(p.get_all_weighted_values(3))