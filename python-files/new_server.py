from inventory import create_ansible_inventory

def new_server():
    server = []
    try:
        ip = input("Enter IP: ")
        user = input("Enter user: ")
        sshpass = input("Enter sshpass: ")
        sudopass = input("Enter sudopass: ")
        datacenter = input("Enter datacenter: ")
               
        server.append((ip, user, sshpass, sudopass, datacenter))

    except Exception as e:
        print("Error:", str(e))

    try:
        # Write the server information to a file
        with open('../output-files/new.txt', 'w') as file:
            for server in server:
                file.write(','.join(server) + '\n')
        with open('../input-files/info.txt', 'w') as info:
            for server in server:
                info.write(','.join(server) + '\n')

        create_ansible_inventory("../output-files/new.txt")
    except Exception as e:
        print("Error:", str(e))
