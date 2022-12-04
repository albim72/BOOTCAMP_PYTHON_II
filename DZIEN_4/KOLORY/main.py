#stwórz klasę Kolory (moduł), konstruktor (id,nazwa_koloru,paleta)
#dla pól id,nazwa_koloru,paleta stwórz gettery
#w module głównym stwórz instancję klasy Kolory i wyświetl getterami wartości: nazwa_koloru,paleta

from kolory import Kolor

kol = Kolor(45,"czerwony","ABC")
print(f"id: {kol.id}")
print(f"kolor: {kol.kolor}")
print(f"paleta: {kol.paleta}")
