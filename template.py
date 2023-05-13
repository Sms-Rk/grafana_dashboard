dashboard_temp = r'''
{
    "annotations": {
      "list": [
        {
          "builtIn": 1,
          "datasource": {
            "type": "grafana",
            "uid": "-- Grafana --"
          },
          "enable": true,
          "hide": true,
          "iconColor": "rgba(0, 211, 255, 1)",
          "name": "Annotations & Alerts",
          "target": {
            "limit": 100,
            "matchAny": false,
            "tags": [],
            "type": "dashboard"
          },
          "type": "dashboard"
        }
      ]
    },
    "editable": true,
    "fiscalYearStartMonth": 0,
    "graphTooltip": 1,
    "id": 9,
    "links": [],
    "liveNow": false,
    "panels": [
      {
        "datasource": {
          "type": "prometheus",
          "uid": "jrN4GVDVk"
        },
        "description": "Main Monitoring Dashboard For All GPU Servers",
        "flowchartsData": {
          "flowcharts": [
            {
              "allowDrawio": false,
              "bgColor": "#ccccdc",
              "center": true,
              "csv": "## See more information for the syntax at https://drawio-app.com/import-from-csv-to-drawio/\n##\n## Example CSV. Use ## for comments and # for configuration.\n## The following names are reserved and should not be used (or ignored):\n## id, tooltip, placeholder(s), link and label (see below)\n##\n#\n## Node label with placeholders and HTML.\n## Default is '%name_of_first_column%'.\n#\n# label: %name%<br><i style=\"color:gray;\">%position%</i><br><a href=\"mailto:%email%\">Email</a>\n#\n## Node style (placeholders are replaced once).\n## Default is the current style for nodes.\n#\n# style: label;image=%image%;whiteSpace=wrap;html=1;rounded=1;fillColor=%fill%;strokeColor=%stroke%;\n#\n## Parent style for nodes with child nodes (placeholders are replaced once).\n#\n# parentstyle: swimlane;whiteSpace=wrap;html=1;childLayout=stackLayout;horizontal=1;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;\n#\n## Optional column name that contains a reference to a named style in styles.\n## Default is the current style for nodes.\n#\n# stylename: -\n#\n## JSON for named styles of the form {\"name\": \"style\", \"name\": \"style\"} where style is a cell style with\n## placeholders that are replaced once.\n#\n# styles: -\n#\n## Optional column name that contains a reference to a named label in labels.\n## Default is the current label.\n#\n# labelname: -\n#\n## JSON for named labels of the form {\"name\": \"label\", \"name\": \"label\"} where label is a cell label with\n## placeholders.\n#\n# labels: -\n#\n## Uses the given column name as the identity for cells (updates existing cells).\n## Default is no identity (empty value or -).\n#\n# identity: -\n#\n## Uses the given column name as the parent reference for cells. Default is no parent (empty or -).\n## The identity above is used for resolving the reference so it must be specified.\n#\n# parent: -\n#\n## Adds a prefix to the identity of cells to make sure they do not collide with existing cells (whose\n## IDs are numbers from 0..n, sometimes with a GUID prefix in the context of realtime collaboration).\n## Default is csvimport-.\n#\n# namespace: csvimport-\n#\n## Connections between rows (\"from\": source colum, \"to\": target column).\n## Label, style and invert are optional. Defaults are '', current style and false.\n## If placeholders are used in the style, they are replaced with data from the source.\n## An optional placeholders can be set to target to use data from the target instead.\n## In addition to label, an optional fromlabel and tolabel can be used to name the column\n## that contains the text for the label in the edges source or target (invert ignored).\n## The label is concatenated in the form fromlabel + label + tolabel if all are defined.\n## The target column may contain a comma-separated list of values.\n## Multiple connect entries are allowed.\n#\n# connect: {\"from\": \"manager\", \"to\": \"name\", \"invert\": true, \"label\": \"manages\", \\\n#          \"style\": \"curved=1;endArrow=blockThin;endFill=1;fontSize=11;\"}\n# connect: {\"from\": \"refs\", \"to\": \"id\", \"style\": \"curved=1;fontSize=11;\"}\n#\n## Node x-coordinate. Possible value is a column name. Default is empty. Layouts will\n## override this value.\n#\n# left: \n#\n## Node y-coordinate. Possible value is a column name. Default is empty. Layouts will\n## override this value.\n#\n# top: \n#\n## Node width. Possible value is a number (in px), auto or an @ sign followed by a column\n## name that contains the value for the width. Default is auto.\n#\n# width: auto\n#\n## Node height. Possible value is a number (in px), auto or an @ sign followed by a column\n## name that contains the value for the height. Default is auto.\n#\n# height: auto\n#\n## Padding for autosize. Default is 0.\n#\n# padding: -12\n#\n## Comma-separated list of ignored columns for metadata. (These can be\n## used for connections and styles but will not be added as metadata.)\n#\n# ignore: id,image,fill,stroke,refs,manager\n#\n## Column to be renamed to link attribute (used as link).\n#\n# link: url\n#\n## Spacing between nodes. Default is 40.\n#\n# nodespacing: 40\n#\n## Spacing between levels of hierarchical layouts. Default is 100.\n#\n# levelspacing: 100\n#\n## Spacing between parallel edges. Default is 40. Use 0 to disable.\n#\n# edgespacing: 40\n#\n## Name or JSON of layout. Possible values are auto, none, verticaltree, horizontaltree,\n## verticalflow, horizontalflow, organic, circle or a JSON string as used in Layout, Apply.\n## Default is auto.\n#\n# layout: auto\n#\n## ---- CSV below this line. First line are column names. ----\nname,position,id,location,manager,email,fill,stroke,refs,url,image\nEvan Miller,CFO,emi,Office 1,,me@example.com,#dae8fc,#6c8ebf,,https://www.draw.io,https://cdn3.iconfinder.com/data/icons/user-avatars-1/512/users-9-2-128.png\nEdward Morrison,Brand Manager,emo,Office 2,Evan Miller,me@example.com,#d5e8d4,#82b366,,https://www.draw.io,https://cdn3.iconfinder.com/data/icons/user-avatars-1/512/users-10-3-128.png\nRon Donovan,System Admin,rdo,Office 3,Evan Miller,me@example.com,#d5e8d4,#82b366,\"emo,tva\",https://www.draw.io,https://cdn3.iconfinder.com/data/icons/user-avatars-1/512/users-2-128.png\nTessa Valet,HR Director,tva,Office 4,Evan Miller,me@example.com,#d5e8d4,#82b366,,https://www.draw.io,https://cdn3.iconfinder.com/data/icons/user-avatars-1/512/users-3-128.png\n",
              "download": false,
              "editorTheme": "dark",
              "editorUrl": "https://www.draw.io",
              "enableAnim": true,
              "grid": false,
              "lock": true,
              "name": "Main",
              "scale": true,
              "tooltip": true,
              "type": "xml",
              "url": "http://<YourUrl>/<Your XML/drawio file/api>",
              "xml": "",
              "zoom": "100%"
            }
          ]
        },
        "format": "short",
        "graphId": "flowchart_2",
        "gridPos": {
          "h": 17,
          "w": 24,
          "x": 0,
          "y": 0
        },
        "id": 2,
        "newFlag": false,
        "rulesData": {
          "rulesData": []
        },
        "targets": [
          {
            "datasource": {
              "type": "prometheus",
              "uid": "jrN4GVDVk"
            },
            "editorMode": "code",
            "expr": "node_load5",
            "hide": false,
            "legendFormat": "CPU{{server}}",
            "range": true,
            "refId": "Cpu Usage"
          },
          {
            "datasource": {
              "type": "prometheus",
              "uid": "jrN4GVDVk"
            },
            "editorMode": "code",
            "expr": "(node_memory_MemTotal_bytes - node_memory_MemFree_bytes - (node_memory_Cached_bytes + node_memory_Buffers_bytes + node_memory_SReclaimable_bytes)) / (node_memory_MemTotal_bytes)) * 100",
            "hide": false,
            "legendFormat": "MEMORY{{server}}",
            "range": true,
            "refId": "Memory Usage"
          },
          {
            "datasource": {
              "type": "prometheus",
              "uid": "jrN4GVDVk"
            },
            "editorMode": "builder",
            "exemplar": false,
            "expr": "nvidia_smi_utilization_gpu_ratio",
            "hide": false,
            "legendFormat": "GPU{{server}}",
            "range": true,
            "refId": "Gpu Utilization"
          }
        ],
        "title": "GPU Servers",
        "transparent": true,
        "type": "agenty-flowcharting-panel",
        "valueName": "current",
        "version": "0.9.0"
      }
    ],
    "refresh": false,
    "schemaVersion": 37,
    "style": "dark",
    "tags": [
      "all",
      "gpu",
      "prod"
    ],
    "templating": {
      "list": [
        {
          "current": {
            "selected": false,
            "text": "node10",
            "value": "node10"
          },
          "datasource": {
            "type": "prometheus",
            "uid": "jrN4GVDVk"
          },
          "definition": "label_values(server)",
          "hide": 0,
          "includeAll": false,
          "label": "server",
          "multi": false,
          "name": "server",
          "options": [],
          "query": {
            "query": "label_values(server)",
            "refId": "StandardVariableQuery"
          },
          "refresh": 1,
          "regex": "",
          "skipUrlSync": false,
          "sort": 0,
          "type": "query"
        }
      ]
    },
    "time": {
      "from": "now-6h",
      "to": "now"
    },
    "timepicker": {},
    "timezone": "",
    "title": "GPU Servers",
    "uid": "jduzo2v4z",
    "version": 72,
    "weekStart": ""
}
'''

rule_temp = r'''
{
    "aggregation": "current",
    "alias": "",
    "colors": [
        "rgba(50, 172, 45, 0.97)",
        "rgba(237, 129, 40, 0.89)",
        "rgba(245, 54, 54, 0.9)"
    ],
    "column": "Time",
    "dateFormat": "YYYY-MM-DD HH:mm:ss",
    "decimals": 2,
    "eventData": [],
    "eventProp": "id",
    "eventRegEx": false,
    "gradient": false,
    "hidden": false,
    "invert": true,
    "linkData": [
        {
            "hidden": false,
            "linkOn": "a",
            "linkParams": false,
            "linkUrl": "",
            "pattern": ""
        }
    ],
    "linkProp": "id",
    "linkRegEx": true,
    "mappingType": 1,
    "metricType": "serie",
    "order": 1,
    "overlayIcon": true,
    "pattern": "",
    "rangeData": [],
    "reduce": true,
    "refId": "A",
    "sanitize": false,
    "shapeData": [
        {
                "colorOn": "a",
                "hidden": false,
                "pattern": "",
                "style": "fillColor"
        }
    ],
    "shapeProp": "id",
    "shapeRegEx": true,
    "stringThresholds": [
        "/.*/",
        "/.*/"
    ],
    "textData": [],
    "textProp": "id",
    "textRegEx": true,
    "thresholds": [
        50,
        80
    ],
    "tooltip": true,
    "tooltipColors": true,
    "tooltipLabel": "",
    "tooltipOn": "a",
    "tpDirection": "v",
    "tpGraph": true,
    "tpGraphScale": "linear",
    "tpGraphSize": "100%",
    "tpGraphType": "line",
    "type": "number",
    "unit": "short",
    "valueData": []
}'''

