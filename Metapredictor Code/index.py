import requests
import json

response = requests.get('http://www.disprot.org/ws/get/DP00004')
print(response)
#response.content



#data = response.json()
#print(data)
#json.loads converts json string to py obj
#content = json.loads(response.content)
#print(content.paper)
