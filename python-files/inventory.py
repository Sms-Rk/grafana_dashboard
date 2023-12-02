import yaml
from runner import runner
import os

def create_ansible_inventory(file_path):
    inventory = {
        'all': {
            'hosts': {},
            'children': {}
        }
    }
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                try:
                    ip, user, sshpass, sudopass, datacenter = line.strip().split(',')
                    host_entry = {
                        'ansible_user': user,
                        'ansible_password': sshpass,
                        'ansible_become': True,
                        'ansible_become_password': sudopass,
                    }
                    
                    if datacenter not in inventory['all']['children']:
                        inventory['all']['children'][datacenter] = {'hosts': {}}
                    
                    inventory['all']['children'][datacenter]['hosts'][ip] = host_entry
                except ValueError:
                    print(f"Invalid line format: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    
    inventory['all']['hosts'] = None
    
    with open('../../Ansible/inventory.yaml', 'w') as file:
        yaml.dump(inventory, file, default_flow_style=False, sort_keys=False)

    #inventory_path = os.path.abspath(os.path.join(os.getcwd(), output_file))
    runner('../../Ansible/inventory.yaml')

# Example usage
#create_ansible_inventory('Monitoring\Grafana_Dashboard\info.txt')
