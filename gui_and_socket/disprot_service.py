import requests
import json
import re

# This function is parsing the data given from the server
def prepare_sequence(data):
    if data == "Not found.":
        return
    #TODO: parse 

# This function is fetching the data from the DISPROT server 
def get_sequence_info(id):
    response = requests.get('http://www.disprot.org/ws/get/' + id)
    #print(response)
    #data = response.json()
    data = json.loads(response.content)
    print(re.search("200", str(response)))
    if re.search("200", str(response)) == None:
        data = "Not found."
    #json.loads converts json string to py obj
    #content = json.loads(response.content)
    #print(content)
    prepare_sequence(data)
    return data








