from xml.etree.ElementTree import Element,SubElement
import xml.etree.ElementTree as ET
from prettyfy import pretty

top = Element("autokomis")

#samochod 1
auto1 = SubElement(top,'samochod')

id = SubElement(auto1,'id')
id.text = 'sam1'

marka = SubElement(auto1,'marka')
marka.text = 'Subaru'

model = SubElement(auto1,'model')
model.text = 'Impreza'

poj = SubElement(auto1,'pojemnosc')
poj.text = '2.0'

rocznik = SubElement(auto1,'rocznik')
rocznik.text = '1999'

cena = SubElement(auto1,'cena')
cena.text = '57800'

wyp_dod = SubElement(auto1,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czarna perła'

klima = SubElement(wyp_dod,'klima')
klima.text = 'FER6435345'

#samochod 2
auto2 = SubElement(top,'samochod')

id = SubElement(auto2,'id')
id.text = 'sam2'

marka = SubElement(auto2,'marka')
marka.text = 'Subaru'

model = SubElement(auto2,'model')
model.text = 'Outback'

poj = SubElement(auto2,'pojemnosc')
poj.text = '2.4'

rocznik = SubElement(auto2,'rocznik')
rocznik.text = '2018'

cena = SubElement(auto2,'cena')
cena.text = '162000'

wyp_dod = SubElement(auto2,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czerwony metallic'

klima = SubElement(wyp_dod,'klima')
klima.text = 'FER6435989008'

pod = SubElement(wyp_dod,'dodatkowe_pod')
pod.text = '4'

print(pretty(top))

with open("subaru_komis.xml","w",encoding="utf-8") as f:
    f.write(pretty(top))
