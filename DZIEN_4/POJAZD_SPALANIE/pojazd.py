from IPojazd import IPojazd

class Pojazd(IPojazd):
    def spalanie_100(self, odl, litry):
        return litry*100/odl

    def koszt_przejazdu(self, odl, litry, cena_l):
        return self.spalanie_100(odl,litry)*(odl/100)*cena_l
