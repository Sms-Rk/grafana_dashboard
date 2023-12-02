import ansible_runner
import os
from mergifile import merge_and_separate_files
from update_inventory import update_inventory_with_python_interpreter
from prom_creator import prom_create
playbook = './playbook.yaml'

def on_completed(runner):
    # Code to execute after the playbook run completes
    try:
        prom_create()
        merge_and_separate_files('../input-files/servers.txt', '../input-files/info.txt', '../output-files/server_file.txt', '../output-files/vm_file.txt')
        update_inventory_with_python_interpreter('../input-files/servers.txt','../../Ansible/inventory.yaml')
        # Add your desired Python code here
    except Exception as e:
        print("Error occurred during post-playbook processing:", str(e))


def runner(inventory):
    #script_directory = os.path.dirname(__file__)
    #playbook_path = os.path.abspath(os.path.join(script_directory, "playbook.yaml"))

    try:
        execution = ansible_runner.run(
            playbook=playbook,
            private_data_dir='../../Ansible',
            tags='informations',
            finished_callback=on_completed
        )

        # Access the status, stdout, and stderr of the execution
        status = execution.status
        stdout = execution.stdout
        stderr = execution.stderr

        print("Status:", status)
        # print("Standard Output:", stdout)
        # print("Standard Error:", stderr)
    except Exception as e:
        print("Error occurred during playbook execution:", str(e))

