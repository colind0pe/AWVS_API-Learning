#配置扫描

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

target_id = '3ca25d5e-fa76-4414-a5be-a0776bfba241'
api_url = 'https://192.168.10.135:3443/api/v1/targets/' + target_id + '/configuration'
headers = {
            'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c511f7e118d4e447cbf3e824950b5952b',
            'Content-type': 'application/json'
            'Accept: application/json'
            }
data = {
        "description": "Target configuration default values",
        "proxy": {
            "enabled":"true","protocol":"http","address":"10.77.27.94","port":10809,"username":"","password":""
        },
        "sensor": "false",
        "scan_speed": "fast",
        }
data = bytes(json.dumps(data), 'utf-8')
r = requests.patch(url=api_url, headers=headers, data=data, verify=False)
print(r.status_code)