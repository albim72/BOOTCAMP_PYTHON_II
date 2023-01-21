odp = input("Czy Ziemia jest płaska? Chcesz znać odpowiedź? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self):
    return "Tak! Ziemia jest płaska!"

def odpowiedz_new(self):
    return "Nie! Ziemia jest elipsoidą!"

def brak(self):
    return "brak odpowiedzi"


class SednoOdpowiedzi(type):
    def __init__(cls,clsname,supercls,attribs):
        if  required:
            if clsname == "Kopernik":
                cls.odpowiedz = odpowiedz_new
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak

class Arystoteles(metaclass=SednoOdpowiedzi):pass
class Platon(metaclass=SednoOdpowiedzi):pass
class SwTomasz(metaclass=SednoOdpowiedzi):pass
class Kopernik(metaclass=SednoOdpowiedzi):pass
    # def odpowiedz(self):
    #     return "Nie! Ziemia jest elipsoidą!"

fil1 = Arystoteles()
fil2 = Platon()
fil3 = SwTomasz()
fil4 = Kopernik()

print(f'Filozof {fil1.__class__.__name__} mówi: {fil1.odpowiedz()}')
print(f'Filozof {fil2.__class__.__name__} mówi: {fil2.odpowiedz()}')
print(f'Filozof {fil3.__class__.__name__} mówi: {fil3.odpowiedz()}')
print(f'Filozof {fil4.__class__.__name__} mówi: {fil4.odpowiedz()}')
