import xml.etree.ElementTree as ET
from string import Template
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
    'pageWidth': '1000',
    'pageHeight': '1000',
    'background': 'none',
    'math': '0',
    'shadow': '0'
}

mxcell_attributes = {
    'style': 'sketch=0;points=[[0.015,0.015,0],[0.985,0.015,0],[0.985,0.985,0],[0.015,0.985,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0.25,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0],[0,0.25,0]];verticalLabelPosition=bottom;html=1;verticalAlign=top;aspect=fixed;align=center;pointerEvents=1;shape=mxgraph.cisco19.server;fillColor=#005073;strokeColor=none;fontColor=#000000;',
    'parent': '1',
    'vertex': '1'
}

mxgeo_attributes = {
    'x': '',
    'y': '',
    'width': '27.5',
    'height': '50',
    'as': 'geometry'
}

mxobj_attributes = {
    'label': '',
    'id': '',
    'link': ''
}
mxrec_attributes = {
    'x_data':'0',
    'x_shape':'0',
    'y':'0',
    'id':'',
}
link_url = Template("https://grafana.tip.co.ir/d/$id/$dashboard?orgId=1&var-server=$server")

def create_shape(data,root,centers):
    if len(data)>5:
        width = str(385.5)
        height = str(((len(data)-1) // 5 + 1)*95)
    else:
        width = str(((len(data)-1)*77)+77.5)
        height = str(110)        
#    x_param = int(mxrec_attributes['x'])+20
    if centers == 0:
        mxrec_attributes['x_data'] = str(0)
    else:
        mxrec_attributes['x_data'] = str(float(mxrec_attributes['x_data']) + 20)
    mxcell_rec = ET.SubElement(root, 'mxCell',id=data[0]["datacenter"] ,value=data[0]["datacenter"] ,style="rounded=0;whiteSpace=wrap;html=1;labelPosition=center;verticalLabelPosition=top;align=center;verticalAlign=bottom;" ,vertex="1" ,parent="1")
    mxgeo_rec = ET.SubElement(mxcell_rec,'mxGeometry',x=mxrec_attributes['x_data'],y=mxrec_attributes['y'],width=width ,height=height ,**{'as': "geometry"})
    
    if len(data)>=5:
        mxrec_attributes['x_shape'] = mxrec_attributes['x_data']
        mxrec_attributes['x_data'] = str(float(mxrec_attributes['x_data'])+(385.5))
    else:
        mxrec_attributes['x_shape'] = mxrec_attributes['x_data']
        mxrec_attributes['x_data'] = str(float(mxrec_attributes['x_data'])+((len(data)-1)*77)+77)
    ##############################################################


    subelement_tag = 'mxCell'
    # Define the initial x and y values
    if centers == 0:
        top_left_x = 25
    else :
        top_left_x = 25 + float(mxrec_attributes['x_shape'])

    top_left_y = 25

    # Define the step values for x and y to create the rectangle shape
    cell_width = 77
    cell_height = 90


    rows = len(data) // 5  # Number of complete rows
    extra_symbols = len(data) % 5  # Number of extra symbols for the last row
    server_counter = 0
    for full_line in range(rows):
        
        for shape in range(5):
            mxobj_attributes["id"] = data[server_counter]["name"]
            mxobj_attributes["label"] = data[server_counter]["name"]
            mxobj_attributes["link"] = link_url.substitute(server=data[server_counter]["name"],dashboard=data[server_counter]["dashboard"],id=data[server_counter]["dashboard"])
            mxgeo_attributes["x"] = str(top_left_x + (shape * cell_width))

            mxgeo_attributes["y"] = str(top_left_y)

            mxobg = ET.SubElement(root, 'UserObject', attrib=mxobj_attributes)
            mxcell = ET.SubElement(mxobg, subelement_tag, attrib=mxcell_attributes)

            mxgeo = ET.SubElement(mxcell, 'mxGeometry', attrib=mxgeo_attributes)
            server_counter += 1
        top_left_y += 90
        top_left_x = top_left_x
    if extra_symbols > 0:
        for last_line in range(extra_symbols):
            mxobj_attributes["id"] = data[server_counter]["name"]
            mxobj_attributes["label"] = data[server_counter]["name"]
            mxobj_attributes["link"] = link_url.substitute(server=data[server_counter]["name"],dashboard=data[server_counter]["dashboard"],id=data[server_counter]["dashboard"])
            mxgeo_attributes["x"] = str(top_left_x + (last_line * cell_width))
            mxgeo_attributes["y"] = str(top_left_y)

            mxobg = ET.SubElement(root, 'UserObject', attrib=mxobj_attributes)
            mxcell = ET.SubElement(mxobg, subelement_tag, attrib=mxcell_attributes)

            mxgeo = ET.SubElement(mxcell, 'mxGeometry', attrib=mxgeo_attributes)
            server_counter += 1
