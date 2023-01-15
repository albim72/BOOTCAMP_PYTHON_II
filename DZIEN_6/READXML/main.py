from xml.dom.minidom import parse

dom = parse("dane.xml")
name = dom.getElementsByTagName('name')
kod = dom.getElementsByTagName('kod')
url = dom.getElementsByTagName('url')
haslo = dom.getElementsByTagName('haslo')

print(" ".join(t.nodeValue for t in name[0].childNodes if t.nodeType==t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[0].childNodes if t.nodeType==t.TEXT_NODE))
print(" ".join(t.nodeValue for t in url[0].childNodes if t.nodeType==t.TEXT_NODE))
print(" ".join(t.nodeValue for t in url[1].childNodes if t.nodeType==t.TEXT_NODE))
print(" ".join(t.nodeValue for t in haslo[0].childNodes if t.nodeType==t.TEXT_NODE))
