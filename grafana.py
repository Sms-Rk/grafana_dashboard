import json
import requests
from template import dashboard_temp,rule_temp
from diagram import diagram
from string import Template
import os



dashboard = json.loads(dashboard_temp)
#rule = json.loads(rule_temp)
link_url = Template("https://grafana.tip.co.ir/d/rYdddlPWk/per-gpu-metrics?orgId=1&refresh=1m&var-server=$server&from=now-15m&to=now")
with open('servers.txt') as f:
    for index, line in enumerate(f):
        server_id=(line.strip().split(',')[0])
        server_num=(line.strip().split(',')[1][-3:])
        print(server_num)
        rulenum = 0
        for rulenum in range(3):
            if rulenum == 0:
                rule = json.loads(rule_temp)
                rule["alias"] = "GPU Utils"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"GPUGPU{server_num}"
                rule["tooltipLabel"] = "GPU Utils"
                link = f"GPU{server_num}"
                rule["linkData"][0]["linkUrl"] = link_url.substitute(server=link)
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

            elif rulenum == 1:
                rule = json.loads(rule_temp)
                rule["alias"] = "Memory Usage"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"MEMORYGPU{server_num}"
                rule["tooltipLabel"] = "Memory Usage%"
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

            elif rulenum == 2:
                rule = json.loads(rule_temp)
                rule["alias"] = "CPU Usage"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"CPUGPU{server_num}"
                rule["tooltipLabel"] = "CPU Usage"
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

dashboard["panels"][0]["flowchartsData"]["flowcharts"][0]["xml"] = diagram.strip()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(dashboard, f,ensure_ascii=False, indent=4)



#url = 'http://localhost:3000/api'

#token = os.environ.get('TOKEN')

#headers = {'Authorization': f'Bearer {token}'}
#with open('dashboard.json') as f:
#    dashboard = json.load(f)


#response = requests.post(url + '/dashboards/db', headers=headers, json={'dashboard': dashboard, 'overwrite': True})

#if response.status_code == 200:
#    print('Dashboard loaded successfully!')
#else:
#    print('Error loading dashboard: ', response.content)