import xmltodict

xml_data = """
<student>
    <id>F34354</id>
    <name>
        <firstname>Olga</firstname>
        <lastname>Knap</lastname>
    </name>
    <email>knap@uczelnia.pl</email>
    <class>informatyka</class>
    <subjects>
        <sub1>Sieci neuronowe</sub1>
        <sub2>Programowanie obiektowe</sub2>
    </subjects>
</student>
"""

mydict = xmltodict.parse(xml_data)

print(type(mydict))

print(mydict)

print(mydict['student']['name']['firstname'])
print(mydict['student']['email'])
