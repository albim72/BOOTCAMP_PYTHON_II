def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f'element listy nr {i+1} -> {j}')

def czytaj_dict(dict):
    for x,y in dict.items():
        print(f'pole: {x} -> wartość: {y}')
