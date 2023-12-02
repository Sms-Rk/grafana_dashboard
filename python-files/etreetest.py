import xml.etree.ElementTree as ET
from string import Template
from shape_function import create_shape

# Define the attribute-value pairs
mxgraph_attributes = {
    'dx': '2141',
    'dy': '1020',
    'grid': '0',
    'gridSize': '10',
    'guides': '1',
    'tooltips': '1',
    'connect': '1',
    'arrows': '1',
    'fold': '1',
    'page': '1',
    'pageScale': '1',
    'pageWidth': '1600',
    'pageHeight': '800',
    'background': 'none',
    'math': '0',
    'shadow': '0'
}

def extract_values(data_center, input_file):
    data = []  # Array to store dictionaries
    try:
        with open(input_file, 'r') as file:
            for line in file:
                if data_center == line.strip().split(',')[5]:
                    line = line.strip()  # Remove leading/trailing whitespaces
                    values = line.split(',')  # Split the line by comma
                    
                    # Create a dictionary from the values and append it to the data array
                    entry = {
                        'name': values[1],
                        'type': values[2],
                        'dashboard': values[3],
                        'datacenter': values[5]
                    }
                    data.append(entry)
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except Exception as e:
        print(f"Error occurred during data extraction: {str(e)}")
    return data

def main(input_file):
    try:
        mxGraphModel = ET.Element('mxGraphModel')
    
        # Set the attributes of the mxGraphModel element
        for attr, value in mxgraph_attributes.items():
            mxGraphModel.set(attr, value)
            
        root = ET.SubElement(mxGraphModel, 'root')
        mxcell_parent = ET.SubElement(root, 'mxCell', id="0")
        mxcell_base = ET.SubElement(root, 'mxCell', id="1" ,parent="0")
    
        last_column_values = []
        with open(input_file, 'r') as file:
            for line in file:
                values = line.strip().split(',')
                last_column_values.append(values[-1])
    
        unique_values = list(dict.fromkeys(last_column_values))
        num_unique_values = len(unique_values)
    
        for centers in range(num_unique_values):
            data = extract_values(unique_values[centers], input_file)
            create_shape(data, root, centers)
    
        final = ET.ElementTree(mxGraphModel)
        xml_string = ET.tostring(final.getroot())
        final2 = ET.fromstring(xml_string)
        xml_str = ET.tostring(final2, encoding='unicode')
        ET.indent(final, space="\t", level=0)
        final.write('./tree.xml',encoding="utf-8")
        return xml_string
    
    except Exception as e:
        print(f"Error occurred during XML generation: {str(e)}")

if __name__ == "__main__":
    try:
        main(input_file='input.txt')
    except Exception as e:
        print(f"Error occurred during execution: {str(e)}")
