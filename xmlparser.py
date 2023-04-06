from diagram import diagram

import xml.etree.ElementTree as ET

root = ET.fromstring(diagram)

# Get all the mxCell elements
mx_cells = root.findall(".//mxCell")

for mx_cell in mx_cells:
    if ("value" not in mx_cell.attrib):
        continue
    else:
        print(mx_cell.attrib["id"],",",mx_cell.attrib["value"])

# Print the ids of the mxCell elements
#for mx_cell in mx_cells:
#    print(mx_cell.attrib["id"])