#funkcja kwota(transport,nocleg_wyzywienie,wycieczki,ubezpieczenie,inne,rabat) ->
#--> (transport+nocleg_wyzywienie)*(1-rabat)+wycieczki+ubezpieczenie+inne

def kwota(t,nw,w,u,i,rab=0):
    if rab >= 0 and rab <= 35:
        return (nw + t) * (1 - rab / 100) + w + u + i
    else:
        return "podaj rabat mniejszy niż 36% lub większy od 0"

print("kwota do zapłaty",kwota(100,100,50,50,50),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,25),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,75),"zł")

#przbuduj funkcję kwota tak aby przyjmowała tylko rabat w zakresie <1,35>


#dla rabatu 0 wypisz -> kwota bazowa wynosi: kwota
#dla rabatów pozostałych -> dla rabatu x% kwota do zapłaty wynosi: kwota
rabs = [0,8,10,12,15,20,25]
#dodatkowo: zapisz kwoty które policzyliśmy dla każdego rabatu do tablicy wynik =[]
print("_____________________________________________________")
wynik = []
for r in rabs:
    kw = kwota (1700, 1230, 450, 200, 180, r)

    if r == 0:
        print (f"cena bazowa do zapłaty wynosi: {kw:.2f} zł")
    else:
        print (f"dla rabatu: {r} %, kwota do zapłaty wynosi: {kw:.2f} zł")

    wynik.append(kw)

print(f"tablica wyników/append/: {wynik}")

result = [kwota(1700,1230,450,200,180,r) for r in rabs]
print(f"tablica wyników/list comprehension/: {result}")
