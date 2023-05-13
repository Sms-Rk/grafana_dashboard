import json, requests, os
from template import dashboard_temp,rule_temp
from diagram import diagram
from string import Template

# Constants
DASHBOARD_FILE = 'dashboard.json'
SERVERS_FILE = 'servers.txt'
RULE_TEMPLATE_FILE = 'rule_template.json'
LINK_TEMPLATE = Template("https://grafana.tip.co.ir/d/rYdddlPWk/per-gpu-metrics?orgId=1&refresh=1m&var-server=$server&from=now-15m&to=now")
ALIASES = ['GPU Utils', 'Memory Usage', 'CPU Usage']
PATTERNS = [
    lambda num: f"GPUGPU{num}",
    lambda num: f"MEMORYGPU{num}",
    lambda num: f"CPUGPU{num}"
]

dashboard = json.loads(dashboard_temp)

rule_template = json.loads(rule_temp)

with open(SERVERS_FILE) as f:
    servers = [line.strip().split(',') for line in f]



for server_id, server_name in servers:
    server_num = server_name[-3:]

    rules_data = [
        {
            'alias': ALIASES[i],
            'linkData': [{'pattern': server_id, 'linkUrl': LINK_TEMPLATE.substitute(server=f"GPU{server_num}")}],
            'shapeData': [{'pattern': server_id}],
            'pattern': PATTERNS[i](server_num),
            'tooltipLabel': ALIASES[i]
        } for i in range(3)
    ]

    dashboard["panels"][0]["rulesData"]["rulesData"].extend(rules_data)

dashboard["panels"][0]["flowchartsData"]["flowcharts"][0]["xml"] = diagram.strip()

with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(dashboard, f, ensure_ascii=False, indent=4)
