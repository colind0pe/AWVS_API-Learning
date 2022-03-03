#删除扫描

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api_url = 'https://192.168.10.135:3443/api/v1/scans/'
scan_id = '2a2a9487-abb9-4951-8127-a453ba2d6860'
headers = {
    'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c511f7e118d4e447cbf3e824950b5952b',
    'Content-type': 'application/json'
}
r = requests.delete(url=api_url + scan_id, headers=headers, verify=False)
print (r.status_code)