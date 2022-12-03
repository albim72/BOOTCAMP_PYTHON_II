liczby = [45,-999,1000,0,9,78,344,566,78,-34,-588,12,4,1990,90,67,-3,0]

def pokaz_stat(dane):
    minimum = min(dane)
    maksimum = max(dane)
    rozstep = maksimum-minimum
    n = len(dane)
    suma = sum(dane)
    avg = suma/n
    return minimum,maksimum,rozstep,n,suma,avg

wynik = pokaz_stat(liczby)
print(wynik)

mini,maxi,roz,n,s,a = pokaz_stat(liczby)
print(f'wartość maksymalna: {maxi}, wartość minimalna: {mini}, rozstęp danych: {roz}, liczba elementów: {n}, '
      f'suma elementów: {s}, średnia arytmetyczna: {a:.2f}')
