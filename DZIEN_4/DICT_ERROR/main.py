#Tworzenie słownika opartego na dwóch kolekcjach (lista,krotka) wartości mogą przyjmować tylko typy:
#float i int, pozostałem zachowanie mają być traktowane jako błąd
#napisz dwie klasy błędu: jedna do ograniczeń kolekcji , druga do ograniczeń typów danych w wartościch słowników

from dictionary import CustomInFloatDict
test_1 = CustomInFloatDict()
print(test_1)

# test_2 = CustomInFloatDict({'a','b'},[1,4])
# print(test_2)

# test_3 = CustomInFloatDict(('x','y','z'),(10,'twenty',30))
# print(test_3)

test_3 = CustomInFloatDict(('x','y','z'),(10,20,30))
print(test_3)
