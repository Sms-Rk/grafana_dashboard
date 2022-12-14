import json
import requests
from template import dashboard_temp,rule_temp
from diagram import diagram
from string import Template



dashboard = json.loads(dashboard_temp)
#rule = json.loads(rule_temp)
link_url = Template("https://grafana.tip.co.ir/d/rYdddlPWk/per-gpu-metrics?orgId=1&refresh=1m&var-server=$server&from=now-15m&to=now")
with open('servers.txt') as f:
    for index, line in enumerate(f):
        server_id=(line.strip().split(',')[0])
        server_num=(line.strip().split(',')[1])
        rulenum = 0
        for rulenum in range(3):
            if rulenum == 0:
                rule = json.loads(rule_temp)
                rule["alias"] = "GPU Utils"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"GPUnode{server_num}"
                rule["tooltiplabel"] = "GPU Utils"
                link = f"GPU{server_num}"
                rule["linkData"][0]["linkUrl"] = link_url.substitute(server=link)
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

            elif rulenum == 1:
                rule = json.loads(rule_temp)
                rule["alias"] = "Memory Usage"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"MEMORYnode{server_num}"
                rule["tooltiplabel"] = "Memory Usage%"
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

            elif rulenum == 2:
                rule = json.loads(rule_temp)
                rule["alias"] = "CPU Usage"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"CPUnode{server_num}"
                rule["tooltiplabel"] = "CPU Usage"
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

dashboard["panels"][0]["flowchartsData"]["flowcharts"][0]["xml"] = diagram

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(dashboard, f,ensure_ascii=False, indent=4)



with open('data.json') as json_file:
    json_data = json.load(json_file)
print(type(json_data))
headers = {"Accept": "application/json",
           "Content-Type": "application/json",
           "Authorization": "Bearer eyJrIjoiektabHdnNkk2NjhpbnZzVmlUQ0U5NHhpdDZvNEtpWEkiLCJuIjoidGVzdDIiLCJpZCI6MX0="
           }

#r = requests.get("http://www.localhost:3005", headers=headers)
#print(r.status_code)

url = "http://www.localhost:3005/api/dashboards/db"
r = requests.post(url, data=json.dumps(json_data), headers=headers)
#p = requests.post(url, headers=headers, data=json.dumps(open('data.json', 'rb')))
print(r.status_code)
