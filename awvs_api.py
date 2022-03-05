import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ip = '192.168.10.135'
api_url = 'https://' + ip + ':3443/api/v1'
add_target_url = 'https://' + ip + ':3443/api/v1/targets'
add_scan_url = 'https://' + ip +':3443/api/v1/scans'
get_vul_url = 'https://' + ip + ':3443/api/v1/vulnerabilities'
profile_id= '11111111-1111-1111-1111-111111111111'
# target_address = 'http://testphp.vulnweb.com/'

headers = {
    'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936c511f7e118d4e447cbf3e824950b5952b',
    'Content-type': 'application/json'
    'Accept: application/json'
}

def add_target():
    target_address = input('输入目标地址:') 
    data = {"address": target_address,"description": "test","type": "default","criticality": 30}
    data = bytes(json.dumps(data), 'utf-8')
    rep = requests.post(url=add_target_url, headers=headers, data=data, verify=False).json()
    target_id = rep['target_id']
    return target_id

def config_target(target_id):
    config_url = 'https://' + ip +':3443/api/v1/targets/' + target_id + '/configuration'
    data = {
            "description": "Target configuration default values",
            "proxy": {
                "enabled":"true","protocol":"http","address":"10.200.196.193","port":10809,"username":"","password":""
            },
            "sensor": "false",
            "scan_speed": "fast",
            }
    data = bytes(json.dumps(data), 'utf-8')
    r = requests.patch(url=config_url, headers=headers, data=data, verify=False)

def add_scan(target_id):
    data = {"target_id": target_id, "profile_id": profile_id, "incremental": False,
                        "schedule": {"disable": False, "start_date": None, "time_sensitive": False}}
    data = bytes(json.dumps(data), 'utf-8')
    rep = requests.post(url=add_scan_url, headers=headers, data=data, verify=False).json()

def get_scans():
    r = requests.get(url=add_scan_url, headers=headers, verify=False).json()
    scan_id = r["scans"][0]['scan_id']
    return scan_id

def get_vul():
    r = requests.get(url=get_vul_url, headers=headers, verify=False).json()
    for vuln in r['vulnerabilities']:
            print('漏洞名称:',vuln['vt_name'],',危险等级:',vuln['severity'])

def main():
    # target_id = add_target()
    # config_target(target_id)
    # add_scan(target_id)
    # scan_id = get_scans()
    # print (scan_id)
    get_vul()
main()