def witaj(imie):
    return f"miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik konkursu {imie} zdobył liczbę punktów: {punkty}"

def wyplata(imie,podstawa,dodatek,prowizja):
    print("firma ABC")
    return f"pracownik {imie}, otrzymuje wypłatę: {podstawa + dodatek + prowizja} zł"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",56))
print(osoba(wyplata,"Anna",5600,450,1560))
