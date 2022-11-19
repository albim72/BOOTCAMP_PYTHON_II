#słownik -> asocjacja klucz <-> wartość
samochod = {
    "marka":"Opel",
    "model":"Vectra",
    "rocznik":2008,
    "poj":1.9
}

print(samochod)
print(type(samochod))
print(samochod["model"])
samochod["rocznik"]=2009
print(samochod)
samochod["przebieg"] = 234700
print(samochod)

print(samochod.items())
print(samochod.keys())
print(samochod.values())

print("___________ klucze ____________")
for k in samochod:
    print(k)

print("___________ wartości ____________")
for v in samochod.values():
    print(v)


print("___________ wartości -> I____________")
for v in samochod.values():
    print(v)

print("___________ wartości -> II____________")
for v in samochod:
    print(samochod[v])

print("___________ items() ____________")

for k,v in samochod.items():
    print(k,":",v)


autokomis = {
    "sam1":{
        "marka":"Opel",
        "model":"Vectra",
        "rocznik":2008,
        "poj":1.9
    },
    "sam2":{
        "marka":"Jeep",
        "model":"Cherokee",
        "rocznik":2018,
        "poj":3.8
    },
    "sam3":{
        "marka":"Toyota",
        "model":"Corolla",
        "rocznik":2014,
        "poj":1.4
    }
}
print(autokomis)

for a in autokomis.values():
    print(a)

for a,b in autokomis.items():
    print("______________________")
    print("id samochodu:",a)
    for k,v in b.items():
        print(k,":",v)
