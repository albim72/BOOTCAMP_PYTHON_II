from pojazd import Pojazd

p1 = Pojazd()

odl = float(input("podaj przejechaną odległość: "))
lt = float(input("podaj liczbę spalonych litrów paliwa: "))
cnl = float(input("podaj cenę za litr paliwa: "))

print(f"spalanie paliwa [l/100km]: {p1.spalanie_100(odl,lt):.3f}")
print(f"koszt przejazdu na trasie {odl} km wynosi: {p1.koszt_przejazdu(odl,lt,cnl):.2f} zł")
