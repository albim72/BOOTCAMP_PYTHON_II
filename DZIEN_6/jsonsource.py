import json

osobajson = '{"imie":"Jan","nazwisko":"Kot","wiek":45,"miasto":"Rzeszów"}'
print(osobajson)
print(type(osobajson))
# print(osobajson["imie"])

osoba = json.loads(osobajson)
print(osoba)
print(type(osoba))
print(osoba["miasto"])

samochod = {
    "marka":"Jeep",
    "model":"Cherokee",
    "poj":4.8,
    "rocznik":2019
}

jsonauto = json.dumps(samochod,indent=4)
print(jsonauto)

#dane json -> nazwa.json

with open("auto.json","w",encoding="utf-8") as f:
    f.write(jsonauto)

with open("auto.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)
print(auto_dict["marka"])

print("_________________________________________________")

info = '{"organizacja":"Fundacja BIOTECH","miasto":"Krosno","kraj":"Polska"}'

ekstra = {
    "idprojektu":456,
    "content":"innowacyjne algorytmy AI",
    "wartość":12560000
}

print("połączenie źródła JSON ze słownikiem")

z = json.loads(info)
z.update(ekstra)

infonew = json.dumps(z,indent=4)

with open("fundacja.json","w",encoding="utf8") as f:
    f.write(infonew)
