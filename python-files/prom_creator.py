from ruamel.yaml import YAML

def prom_create():
# Initialize YAML with custom indentation
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)  # customize indentation level

    # Read from file
    with open('../input-files/servers.txt', 'r') as f:
        lines = f.readlines()

    # Create dictionary
    config = {
        'global': {
            'external_labels': {
                'prometheus': 'prom-0'
            },
            'scrape_interval': '15s',
            'evaluation_interval': '15s'
        },
        'scrape_configs': [
            {
                'job_name': 'prometheus',
                'scrape_interval': '5s',
                'static_configs': [
                    {
                        'targets': ['localhost:9090']
                    }
                ]
            },
            {
                'job_name': 'cadvisor',
                'metrics_path': '/cadvisor',
                'static_configs': []
            },
            {
                'job_name': 'gpu',
                'metrics_path': '/gpu',
                'static_configs': []
            },
            {
                'job_name': 'sm',
                'metrics_path': '/sm',
                'static_configs': []
            },
            {
                'job_name': 'ip',
                'metrics_path': '/ip',
                'static_configs': []
            },
            {
                'job_name': 'node',
                'metrics_path': '/node',
                'static_configs': []
            }
        ]
    }

    for line in lines:
        parts = line.strip().split(',')
        config['scrape_configs'][4]['static_configs'].append({
                'targets': [f'{parts[0]}:9117'],
                'labels': {
                    'server': parts[1]
                }
            })
        config['scrape_configs'][5]['static_configs'].append({
                'targets': [f'{parts[0]}:9117'],
                'labels': {
                    'server': parts[1]
                }
            })
        if 'gpu' in parts[3]:
            config['scrape_configs'][2]['static_configs'].append({
                'targets': [f'{parts[0]}:9117'],
                'labels': {
                    'server': parts[1]
                }
            })
            config['scrape_configs'][3]['static_configs'].append({
                'targets': [f'{parts[0]}:9117'],
                'labels': {
                    'server': parts[1]
                }
            })

        if 'docker' in parts[3]:
            config['scrape_configs'][1]['static_configs'].append({
                'targets': [f'{parts[0]}:9117'],
                'labels': {
                    'server': parts[1]
                }
            })

    # Write to file
    with open('../output-files/prometheus.yml', 'w') as f:
        yaml.dump(config, f)
