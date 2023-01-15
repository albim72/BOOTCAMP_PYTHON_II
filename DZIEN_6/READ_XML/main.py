import xml.etree.ElementTree as ET

try:
    tree = ET.parse("kraj.xml")
    root = tree.getroot()
    for child in root:
        print(f'element child, tag: {child.tag}, atrybuty: {child.attrib}')

    print(root[0])
    print(root[0][1].text)
    print(root[2][5].attrib["name"])


except:
    print("element nie istnieje!")
    
