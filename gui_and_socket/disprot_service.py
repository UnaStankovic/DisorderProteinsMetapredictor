import requests
import json
import re

def shortened_sequence(sequence):
    if(sequence[0] == ">"):
        pom = ''.join(sequence.split("\n")[1:])
    else:
        pom = sequence.replace("\n","")
    return pom 

# This function is parsing the data given from the server
def prepare_sequence(data):
    if data == "Not found.":
        return data
    sequence = data['sequence']
    seq_len = len(shortened_sequence(sequence)) 
    intervals = []
    disprot = []
    disprot = ['-'] * seq_len
    for record in data['regions']:
        start_interval = record["start"]
        end_interval = record["end"]
        intervals.append((start_interval, end_interval))
    for interval in intervals:
        begin, end = int(interval[0]), int(interval[1])
        for i in range(begin-1, end):
            disprot[i] = "D"
    return disprot, sequence


    
# This function is fetching the data from the DISPROT server 
def get_sequence_info(id_disp):
   # response = requests.get('http://www.disprot.org/ws/get/' + id_disp) # Old API changed on 13.09.2019.
    response = requests.get('http://www.disprot.org/api/' + id_disp)
    data = json.loads(response.content)
    if re.search("200", str(response)) == None:
        data = "Not found."
    return prepare_sequence(data)








