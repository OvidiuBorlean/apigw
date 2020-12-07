import requests
import json
url = "_url_"

data = {'id': '11', 'hostname': 'test_hostmane', 'status': 'Up'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
