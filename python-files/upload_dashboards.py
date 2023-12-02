import requests
import json

def import_dashboard(json_file_path):
    try:
        api_url = 'https://grafana.tip.co.ir'
        api_key = 'glsa_4PGvfyZhlKHzmkTGVUnsXoMFWOrHc8Dr_b3af1ad2'
        headers = {
            'Authorization': 'Bearer ' + api_key,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        
        with open(json_file_path, 'r') as f:
            json_data = json.load(f)


        url = api_url + '/api/dashboards/db'
        response = requests.post(url, headers=headers, json=json_data)

        print('Request payload:', json.dumps(json_data, indent=2))
        print('Response status code:', response.status_code)

        if response.status_code == 200:
            print('Dashboard imported successfully.')
        else:
            print('Failed to import dashboard.', response.status_code)
            print(response.json())
    except Exception as e:
        print("Error:", str(e))

def uploader():
    with open('../input-files/servers.txt','r') as server:
            lines = server.readlines()

    dashboards = []
    for line in lines:
        dashboard = line.strip().split(',')[3]
        if 'docker' in dashboard:
            docker_found = 1
        dashboards.append(dashboard)

    new_dash = set(dashboards)
    for items in new_dash:
        import_dashboard(f'../json-files/{items}.json')
    if docker_found == 1:
        import_dashboard('../json-files/containers.json')
