nb = [1,2,3,4]
nb_pl = ['jeden','dwa','trzy','cztery','pięć']
nb_eng = ['one','two','three','four']

wynik = zip()
lista_w = list(wynik)
print(lista_w)

wynik = zip(nb,nb_pl,nb_eng)
lista_w = list(wynik)
print(lista_w)

sklep = ['mleko','masło','twaróg','śmietana','marchew']

for tw in sklep:
    print(tw,end=" - ")
print("___________________________")

for i,w in enumerate(sklep,101):
    print(f'nr {i+1}, {w}')
