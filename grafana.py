import json

from template import dashboard_temp,rule_temp


dashboard = json.loads(dashboard_temp)
rule = json.loads(rule_temp)

with open('servers.txt') as f:
    for index, line in enumerate(f):
        server_id=(line.strip().split(',')[0])
        server_num=(line.strip().split(',')[1][-2:])
        rulenum = 0
        for rulenum in range(3):
            rule = json.loads(rule_temp)
            if rulenum == 0:
                rule["alias"] = "GPU Utils"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"GPUnode{server_num}"
                rule["tooltiplabel"] = "GPU Utils"
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

            elif rulenum == 1:
                rule["alias"] = "Memory Usage"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"MEMORYnode{server_num}"
                rule["tooltiplabel"] = "Memory Usage%"
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

            else:
                rule["alias"] = "CPU Usage"
                rule["linkData"][0]["pattern"] = server_id
                rule["shapeData"][0]["pattern"] = server_id
                rule["pattern"] = f"CPUnode{server_num}"
                rule["tooltiplabel"] = "CPU Usage"
                dashboard["panels"][0]["rulesData"]["rulesData"].append(rule)

final_dashboard = json.dumps(dashboard, indent=4)
print(final_dashboard)
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(dashboard, f,ensure_ascii=False, indent=4)