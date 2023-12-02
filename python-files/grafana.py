import json
from template import dashboard_temp, rule_temp
from diagram import diagram
from string import Template
import etreetest

def generate_dashboard(input_file, output_file, type):
    try:
        # Constants
        DASHBOARD_FILE = 'dashboard.json'
        RULE_TEMPLATE_FILE = 'rule_template.json'
        ALIASES = ['GPU Utils', 'Memory Usage', 'CPU Usage']
        ALIASES2 = ['Memory Usage', 'CPU Usage']
        PATTERNS = [
            lambda hostname: f"GPU{hostname}",
            lambda hostname: f"MEMORY{hostname}",
            lambda hostname: f"CPU{hostname}"
        ]
        PATTERNS2 = [
            lambda hostname: f"MEMORY{hostname}",
            lambda hostname: f"CPU{hostname}"
        ]
    
        dashboard = json.loads(dashboard_temp)
        rule_template = json.loads(rule_temp)
    
        hostname = []
        server_type = []
        with open(input_file, 'r') as file:
            for line in file:
                line = line.strip() 
                values = line.split(',')
                hostname.append(values[1])
                server_type.append(values[2])
        def new_func(dashboard, hostname, alias, pattern):
            rule = json.loads(rule_temp)
            rule["alias"] = alias
            rule["pattern"] = pattern(hostname)
            rule["shapeData"][0]["pattern"] = hostname
            rule["tooltipLabel"] = alias
            dashboard["dashboard"]["panels"][0]["rulesData"]["rulesData"].append(rule)
    
        for hostname, server_type in zip(hostname, server_type):
            if server_type == "gpu":
                for alias, pattern in zip(ALIASES, PATTERNS):
                    new_func(dashboard, hostname, alias, pattern)
            else:
                for alias, pattern in zip(ALIASES2, PATTERNS2):
                    new_func(dashboard, hostname, alias, pattern)
    
        with open(DASHBOARD_FILE, 'w', encoding='utf-8') as f:
            json.dump(dashboard, f, ensure_ascii=False, indent=4)
    
        with open(DASHBOARD_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    
        data["dashboard"]["panels"][0]["flowchartsData"]["flowcharts"][0]["xml"] = etreetest.main(input_file).decode('utf-8').replace('\\', '')
        data["dashboard"]["templating"]["list"][0]["definition"] = f"label_values({type})"
        data["dashboard"]["templating"]["list"][0]["query"]["query"] = f"label_values({type})"    
        data["dashboard"]["title"] = f"ALL {type.upper()}1s"
        data["dashboard"]["panels"][0]["title"] = f"ALL {type.upper()}1s"
        data["dashboard"]["panels"][0]["description"] = f"Main Dashboard For ALL {type.upper()}s"
        data["dashboard"]["uid"] = f"all{type}1s"
        data["message"] = f"Dashboard generated for all {type}s"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"Error occurred during dashboard generation: {str(e)}")

## Example usage
#try:
#    generate_dashboard(input_file='Monitoring\Grafana_Dashboard\output-files\server_file.txt', output_file='output.json', type='server')
#except Exception as e:
#    print(f"Error occurred during dashboard generation: {str(e)}")
