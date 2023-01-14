class Samochod:
    def __init__(self,marka,model,rocznik,cena,rata):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.cena = cena
        self.rata = rata

    @staticmethod
    def salon(miasto):
        return f'salon sprzedaży -> {miasto}'

    @classmethod
    def obliczenie_raty(cls,cena,lrat):
        return cls("Opel","Insignia",2020,156000,1.3*cena/lrat)

sm = Samochod("Opel","Insignia",2020,156000,1432)
print(sm.salon("Trouń"))
print(sm.rata)

smc = Samochod.obliczenie_raty(178900,64)
print(smc.salon("Lublin"))
print(smc.rata)
