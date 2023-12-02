import yaml


def update_inventory_with_python_interpreter(file_path, inventory_path):
    # Read the first file and create a dictionary with IP addresses and Python interpreters
    interpreters = {}
    with open(file_path, 'r') as file:
        for line in file:
            ip, _, _, _, interpreter = line.strip().split(',')
            interpreters[ip] = interpreter
    # Read the inventory file and update with ansible_python_interpreter
    with open(inventory_path, 'r') as inv_file:
        inventory_data = yaml.safe_load(inv_file)
    for group in inventory_data.get('all', {}).get('children', {}).values():
        for host, host_vars in group.get('hosts', {}).items():
            if ip in interpreters:
                host_vars['ansible_python_interpreter'] = interpreters[ip]

    # Write the updated inventory back to the file
    with open(inventory_path, 'w') as inv_file:
        yaml.dump(inventory_data, inv_file, sort_keys=True, indent=2)
