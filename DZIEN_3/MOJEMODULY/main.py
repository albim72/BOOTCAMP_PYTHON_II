# import dane as dn
from dane import nr_filii,book
from lib_funkcje.bfunkcje import czytaj_liste,czytaj_dict
from lib_klasy.cdane import CDane

print(nr_filii)
print(book)
print("_________ czytanie przez funkcje ____________")
czytaj_liste(nr_filii)
print("______________________")
czytaj_dict(book)
print("_________ czytanie przez klasę ____________")
cd = CDane(nr_filii,book)
cd.czytaj_l()
cd.czytaj_d()
