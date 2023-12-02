from grafana import generate_dashboard
from upload_dashboards import import_dashboard


def merge_and_separate_files(first_file_path, second_file_path, server_file_path, vm_file_path):
    try:
        # Read contents of the first file
        with open(first_file_path, 'r') as first_file:
            first_lines = first_file.readlines()
        
        # Read contents of the second file
        with open(second_file_path, 'r') as second_file:
            second_lines = second_file.readlines()            
        
        # Create an empty list to store merged lines
        merged_lines = []
    
        # Create empty lists to store server and vm lines
        server_lines = []
        vm_lines = []
    
        # Iterate over each line in the first file
        for first_line in first_lines:
            # Split the line into sections
            first_sections = first_line.strip().split(',')
    
            # Extract the first section
            first_section = first_sections[0]
    
            # Iterate over each line in the second file
            for second_line in second_lines:
                # Split the line into sections
                second_sections = second_line.strip().split(',')
    
                # Extract the first section
                second_section = second_sections[0]
    
                # Check if the first sections match
                if first_section == second_section:
                    # Merge the lines
                    merged_line = ','.join([first_section] + first_sections[1:] + second_sections[-1:])
                    merged_lines.append(merged_line)
    
                    # Check if "server" is present in the third section
                    if "server" in first_sections[3]:
                        server_lines.append(merged_line)
                    # Check if "vm" is present in the third section
                    elif "vm" in first_sections[3]:
                        vm_lines.append(merged_line)
    
                    break  # Stop searching for matching lines
    
        if server_lines:
            # Write server lines to the server file
            with open(server_file_path, 'w') as server_file:
                server_file.writelines('\n'.join(server_lines))
            generate_dashboard("../output-files/server_file.txt","../json-files/all_servers.json","server")
            import_dashboard("../json-files/all_servers.json")
    
        if vm_lines:
            # Write vm lines to the vm file
            with open(vm_file_path, 'w') as vm_file:
                vm_file.writelines('\n'.join(vm_lines))
            generate_dashboard("../output-files/vm_file.txt","../json-files/all_vms.json","vm")
            import_dashboard("../json-files/all_vms.json")

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"Error occurred during file processing: {str(e)}")


# Usage example
#try:
#    merge_and_separate_files('Monitoring\Grafana_Dashboard\servers.txt', 'Monitoring\Grafana_Dashboard\info.txt', 'server_file.txt', 'vm_file.txt')
#except Exception as e:
#    print(f"Error occurred during execution: {str(e)}")
