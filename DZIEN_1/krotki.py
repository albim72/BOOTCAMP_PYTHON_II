animal = ("kot","pies","szynszyla","papuga","tygrys","boa")
print(animal)
print(type(animal))
print(animal[5])
print(animal[2:4])


if "papuga" in animal:
    print("tak! papuga to zwierz...")

if "budynek" in animal:
    print("to jest błąd!")

print("pies" in animal)
anim2 = ("pająk","mucha")

animal = animal + anim2

print(animal)

mojakrotka = tuple(("obiekt56",67,89,10.05545,True,"Urszula"))
print(mojakrotka)

#zmodyfikuj krotkę: usuń wartość 89, zamień imię "Urszula" na "Karol"
#wstaw na pozycji 4 wartość 100, wastaw na końcu listy False

mojalista = list(mojakrotka)
mojalista.remove(89)
ur = mojalista.index("Urszula")
mojalista[ur] = "Karol"
mojalista.insert(4,100)
mojalista.append(False)

mojakrotka = tuple(mojalista)
print(mojakrotka)
