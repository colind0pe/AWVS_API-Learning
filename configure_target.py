import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api_url = 'https://192.168.10.135:3443/api/v1/targets/8251b9af-d2b0-4e08-9280-7a4516f26bb2/configuration'
headers = {
            'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c511f7e118d4e447cbf3e824950b5952b',
            'Content-type': 'application/json'
            'Accept: application/json'
            }
data = {
        "description": "Target configuration default values",
        "proxy": {
            "enabled":"true","protocol":"http","address":"127.0.0.1","port":10809,"username":"","password":""
        },
        "sensor": "false",
        "scan_speed": "fast",
        }
data = bytes(json.dumps(data), 'utf-8')
r = requests.patch(url=api_url, headers=headers, data=data, verify=False)