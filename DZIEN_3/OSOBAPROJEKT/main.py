from osoba import Osoba
from pracownik import Pracownik
from student import Student


za = 8
print("______________ nowa osoba ________________")
os1 = Osoba("Jan",36,99,173)
os1.print_osoba()
print(f"wiek za {za} lat: {os1.wiek_za_x_lat(za)}")
print(f"czy osoba jest pracownikiem? ({os1.czypracownik()})")

print("______________ nowa osoba ________________")
os2 = Osoba("Olga",30,53,168)
os2.setkolor("niebieskie")
os2.print_osoba()
print(f"wiek za {za} lat: {os2.wiek_za_x_lat(za)}")
print(f"czy osoba jest pracownikiem? ({os2.czypracownik()})")

print("______________ nowy pracownik ________________")
pr1 = Pracownik("Karol",50,94,174,"ABC","dyrektor",13,11900)
pr1.print_osoba()
pr1.print_pracownik()
print(f"wiek za {za} lat: {pr1.wiek_za_x_lat(za)}")
print(f"czy osoba jest pracownikiem? [{pr1.czypracownik()}]")

print("______________ nowy student ________________")
st1 = Student("Olaf",22,77,177,55345,"budowlany","budowa mostów",3)
st1.print_osoba()
st1.print_student()
print(f"wiek za {za} lat: {st1.wiek_za_x_lat(za)}")
print(f"czy osoba jest pracownikiem? [{st1.czypracownik()}]")

print("___a___________ nowy student ________________")
st2 = Student("Olga",23,62,172,566546,"nauk społecznych","socjologia",4,
              "XYZ","sekretarka",1,2600)
st2.print_osoba()
st2.print_student()
st2.print_pracownik()
print(f"wiek za {za} lat: {st2.wiek_za_x_lat(za)}")
print(f"czy osoba jest pracownikiem? [{st2.czypracownik()}]")
