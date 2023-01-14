from dataclasses import dataclass

class Liczba:
    def __init__(self,x):
        self.x = x

zko = Liczba(2)
print(zko.x)

@dataclass
class DLiczba:
    x:int

dko = DLiczba(6.7)
print(dko.x)

@dataclass
class Dane:
    nazwa:str
    licznik:int = 0
    cena:float = 0.0

prod = Dane("pudełko nr 5",6,11.2)
print(f'{prod.nazwa} -> {prod.cena} zł -> {prod.licznik} sztuk')
