#przykład 1

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

#przykład 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników"
    def brak():
        return "jeśli nie uiścisz opłaty startowej w ciągu 3 dni zostaniesz skreslony z listy"
    def error():
        return "właściwe oznaczenia: 1 - wpłata, 0 - brak wpłaty"
    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print("_______________________________________")
print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(111)())

print("_______________________________________")

#przykład 3

def startstop(funkcja):
    def wrapper(*args):
        print("_________________________")
        print("startowanie procesu.....")
        funkcja(*args)
        print("kończenie procesu")
        print("_________________________")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka....")

zw = startstop(zawijanie)
zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na urodziny....")

dmuchanie("baloników")

@startstop
def fx(n):
    print(f'{n**8-2}')

fx(12)
