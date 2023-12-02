import ansible_runner
def role_runner():
    try:
        r = ansible_runner.run(
            private_data_dir='../../Ansible',
            playbook='./playbook.yaml',
            tags='all-thing-together'
            )
    except Exception as e:
        print("Error occurred during playbook execution:", str(e))
