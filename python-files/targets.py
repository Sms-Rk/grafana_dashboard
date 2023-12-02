import json

# Define the target and job combinations
PATTERN = [
    {"type":"server","port":"9100"},
    {"type":"gpu","port":"9835"},
    {"type":"gpu","port":"9009"},
    {"type":"docker","port":"8080"}
]

target = []

with open('../input-files/servers.txt', 'r') as file:
    for line in file:
        first_value, third_value = line.strip().split(',')[1::2]
        ip_address = line.strip().split(',')[0]
        exporters = third_value.split('-')
        ip_list = []
        
        for value in exporters:
            ports = [item["port"] for item in PATTERN if item["type"] == value]
            if ports:
                ip_list.extend([f"{ip_address}:{port}" for port in ports])

        if ip_list:
            label_key = "server" if "server" in exporters else "vm"
            obj = {
                "targets": ip_list,
                "label": {
                    label_key: first_value,
                }
            }
            target.append(obj)

# Convert the list to a JSON string
json_data = json.dumps(target, indent=4)
with open("output.json", "w") as file:
    file.write(json_data)
