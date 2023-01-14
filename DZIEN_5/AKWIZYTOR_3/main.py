from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class MainAkwizytor:

    def __repr__(self):
        return "jestem właścicielem firmy i mam własną dywidendę..."

    def zarobek(self):
        return Decimal('1_000_000.00')

k = MainAkwizytor()
s = AkwizytorNaEtacie('Leon','Nowak',7564545654,Decimal('356000.0'),Decimal(3.5),Decimal('3500'))
c = Akwizytor('Olga','Kot',74563456,Decimal('554900'),Decimal(5.7))

pracownicy = [c,s,k]

for pr in pracownicy:
    print(pr)
    print(f'{pr.zarobek():,.2f} zł\n')
