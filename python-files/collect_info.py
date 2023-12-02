from inventory import create_ansible_inventory
import requests
import json
from role_runner import role_runner
from new_server import new_server
from upload_dashboards import uploader
def enter_file_address():
    try:
        file_address = input("Enter file address: ")
        # Do something with the file address
        print("File address:", file_address)
        create_ansible_inventory(file_address)
    except Exception as e:
        print("Error:", str(e))

def enter_servers_manually():
    info = []
    while True:
        try:
            ip = input("Enter IP: ")
            user = input("Enter user: ")
            sshpass = input("Enter sshpass: ")
            sudopass = input("Enter sudopass: ")
            datacenter = input("Enter datacenter: ")
            
            # Input validation
            if not ip or not user or not sshpass or not sudopass or not datacenter:
                print("Invalid input. Please provide all the required information.")
                continue
            
            info.append((ip, user, sshpass, sudopass, datacenter))

            choice = input("Do you want to enter more servers? (y/n): ")
            if choice.lower() != 'y':
                break
        except Exception as e:
            print("Error:", str(e))

    try:
        # Write the server information to a file
        with open('../input-files/info.txt', 'w') as file:
            for server in info:
                file.write(','.join(server) + '\n')

        create_ansible_inventory("../input-files/info.txt")
    except Exception as e:
        print("Error:", str(e))


def main():
    try:
        start = input("is this first time you want to run application or you want add some servers?? (first/add): ")
        if start.lower() == 'first':
            choice = input("Do you want to enter a file address or enter servers manually? (file/manual): ")
            if choice.lower() == 'file':
                enter_file_address()
            elif choice.lower() == 'manual':
                enter_servers_manually()
            else:
                print("Invalid choice")
        elif start.lower() == 'add':
            new_server()
        else:
            print("Invalid choice")
    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':

    try:   
        main()
        role_runner()
        uploader()
    except Exception as e:
        print("Error:", str(e))
