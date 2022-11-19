automarka = ["Mercedes","Landrover","Jeep","Fiat","BMW","Opel","Honda","Toyota"]
print(automarka)
print((automarka[3]))
print((automarka[-2]))
print((automarka[-4:]))

automarka.append("Seat")
print(automarka)

automarka.insert(3,"Renault")
print(automarka)

automarka[automarka.index("Fiat")] = "Alfa Romeo"
print(automarka)

automarka.remove("Landrover")
print(automarka)

del automarka[0]
print(automarka)

automarka.sort()
print(automarka)

automarka.reverse()
print(automarka)

automarka.sort(reverse=True)
print(automarka)
automarka.extend(["Aston Martin","Kia","Volvo"])
print(automarka)

mk = automarka
mk1 = list(automarka)
mk2 = automarka[:]
print("start:",mk)
print("start:",mk1)
print("start:",mk2)
print("start:",automarka)

automarka[2:5] = [45,78,True,7.777,5,6,"Vacant"]
print("koniec:",mk)
print("koniec:",mk1)
print("koniec:",mk2)
print("koniec:",automarka)

am = automarka.index("Aston Martin")
print(am)
print(automarka[am])

odrot = automarka[am][::-1]
print(odrot)

#utwórz dwie listy: parz i nieparz
#do listy parz wstaw pozycje z listy automarka o wartościach parzystych inseksów położeń
#do listy nieparz wstaw pozycje z listy automarka o wartościach nieparzystych inseksów położeń

parz = automarka[::2]
nieparz = automarka[1::2]

print(parz)
print(nieparz)
