from IPojazd import IPojazd
from IDane import IDane

class Pojazd(IPojazd,IDane):
    def __init__(self,marka,model,rocznik,cena):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.cena = cena

    def spalanie_100(self, odl, litry):
        return litry*100/odl

    def koszt_przejazdu(self, odl, litry, cena_l):
        return self.spalanie_100(odl,litry)*(odl/100)*cena_l

    def opispojazdu(self):
        return f"Pojazd marki {self.marka} model {self.model}, rocznik: {self.rocznik}, cena: {self.cena} zł"

    def silnik(self, rodzaj, poj, l_km):
        return f"silnik {rodzaj}, pojemność: {poj},liczba przejechanych kilometrów: {l_km}"

