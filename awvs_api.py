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
                "enabled":"true","protocol":"http","address":"10.77.27.94","port":10809,"username":"","password":""
            },
            "sensor": "false",
            "scan_speed": "fast",
            }
    data = bytes(json.dumps(data), 'utf-8')
    r = requests.patch(url=config_url, headers=headers, data=data, verify=False)
    return r.status_code

def add_scan(target_id):
    data = {"target_id": target_id, "profile_id": profile_id, "incremental": False,
                        "schedule": {"disable": False, "start_date": None, "time_sensitive": False}}
    data = bytes(json.dumps(data), 'utf-8')
    rep = requests.post(url=add_scan_url, headers=headers, data=data, verify=False).json()

def get_scans(list_scan_id=[]):
    r = requests.get(url=add_scan_url, headers=headers, verify=False).json()
    for scan_id in r['scans']:
        list_scan_id.append(scan_id['scan_id'])
    return ("\n".join(list_scan_id))

def get_vul(High=0,Medium=0,Low=0):
    r = requests.get(url=get_vul_url, headers=headers, verify=False).json()
    for vuln in r['vulnerabilities']:
        if vuln['severity'] == 3 :
            High = High + 1
        if vuln['severity'] == 2 :
            Medium = Medium + 1
        if vuln['severity'] == 1 :
            Low = Low + 1
        else :
            continue
    return High,Medium,Low


def main():
    # target_id = add_target()
    # config_target(target_id)
    # add_scan(target_id)
    # list_scan_id = get_scans()
    # print (list_scan_id)
    # High,Medium,Low = get_vul()
    # print(High,Medium,Low)
main()