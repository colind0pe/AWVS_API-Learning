from importlib.resources import path
import requests
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ip = '192.168.10.135'
api_url = 'https://' + ip + ':3443/api/v1'
add_target_url = 'https://' + ip + ':3443/api/v1/targets'
add_scan_url = 'https://' + ip +':3443/api/v1/scans'
get_vul_url = 'https://' + ip + ':3443/api/v1/vulnerabilities'
generate_report_url = 'https://' + ip + ':3443/api/v1/reports'
profile_id= '11111111-1111-1111-1111-111111111111'
template_id = '11111111-1111-1111-1111-111111111113'
# target_address = 'http://testphp.vulnweb.com/'


headers = {
    'X-Auth': '1986ad8c0a5b3df4d7028d5f3c06e936ccebaf974cea34b73a87b08f5f7d10cdf',
    'Content-type': 'application/json'
    'Accept: application/json'
}


def add_target():
    target_address = input('') 
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
        vul_num = {"High":High,"Medium":Medium,"Low":Low}
        return vul_num


def vul_type(sql=0,lfi=0,xss=0,path=0):
    r = requests.get(url=get_vul_url, headers=headers, verify=False).json()
    for vuln in r['vulnerabilities']:
        if vuln['vt_name'] == 'SQL 注入':
            sql = sql + 1
        if vuln['vt_name'] == '文件包含':
            lfi = lfi + 1
        if vuln['vt_name'] == '目录穿越':
            path = path + 1
        if vuln['vt_name'] == '跨站脚本':
            xss = xss + 1
        else :
            continue
        vul_type = sql,lfi,xss,path
        return vul_type
        # print(vuln['vt_name'])



def get_report():
    data = {
            "template_id": template_id,
            "source": {
                "description": "test",
                "list_type": "scans",
                "id_list": [
                '1b617788-12b8-49b2-b778-8cc442990214'
                ]
            }
            }
    data = bytes(json.dumps(data), 'utf-8')
    rep = requests.post(url=generate_report_url, headers=headers, data=data, verify=False).json()
    report_id = rep['report_id']
 

def main():
    # target_id = add_target()
    # config_target(target_id)
    # add_scan(target_id)
    # list_scan_id = get_scans()
    # print (list_scan_id)
    vul_num = get_vul()
    print(vul_num)
    # global vul_type
    # vul_type = vul_type()
    # print (vul_type)
    # get_report()
main()