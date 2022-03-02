import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api_url = 'https://192.168.10.135:3443/api/v1/targets'
headers = {
    'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c511f7e118d4e447cbf3e824950b5952b',
    'Content-type': 'application/json'
    'Accept: application/json'
}
data = {"address": "http://testphp.vulnweb.com/","description": "test","type": "default","criticality": 30}
data = bytes(json.dumps(data), 'utf-8')
rep = requests.post(url=api_url, headers=headers, data=data, verify=False)
print(rep.json()) 