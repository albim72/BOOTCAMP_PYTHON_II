#n!=1*2*....*n
#doble -> 1.8E308
#????n -> 171!
import sys
from dziedzinasilnia import DziedzinaSilnia
sys.set_int_max_str_digits(1000000000)
sys.setrecursionlimit(0x10000000)

def silnia(n):
    if n<0:
        raise DziedzinaSilnia(n)
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n<0:
        raise DziedzinaSilnia(n)
    if n == 0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f"silnia z n={n} wynosi: {silnia(n)}")
    print(f"silnia rekurencyjna z n={n} wynosi: {silnia_rek(n)}")
except DziedzinaSilnia as ve:
    print(ve)

#napisz klasę błędu DziedzinaSilnia. która będzie reagować na zadanie wartości ujemnych argumentu n
#wepnij klasę błędu w rozwiązanie
