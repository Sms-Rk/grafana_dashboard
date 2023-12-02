# download this file and unzip before building dockerfile
# https://storage.googleapis.com/plugins-community/agenty-flowcharting-panel/release/0.9.1/agenty-flowcharting-panel-0.9.1.zip
FROM grafana/grafana:10.0.1

# labels
LABEL maintainer="Targoman"
LABEL description="Grafana with preinstalled flowcharting plugin"

# Copy the plugin to the container
copy agenty-flowcharting-panel /var/lib/grafana/plugins/agenty-flowcharting-panel
