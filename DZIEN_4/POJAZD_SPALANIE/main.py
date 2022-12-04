from pojazd import Pojazd

p1 = Pojazd("Opel","Insignia",2019,53400)


sln = ("diesel",1.9,234500)
odl = float(input("podaj przejechaną odległość: "))
lt = float(input("podaj liczbę spalonych litrów paliwa: "))
cnl = float(input("podaj cenę za litr paliwa: "))

print(f"dane pojazdu: {p1.opispojazdu()}")
print(f"dane silnika: {p1.silnik(sln[0],sln[1],sln[2])}")
print(f"spalanie paliwa [l/100km]: {p1.spalanie_100(odl,lt):.3f}")
print(f"koszt przejazdu na trasie {odl} km wynosi: {p1.koszt_przejazdu(odl,lt,cnl):.2f} zł")
