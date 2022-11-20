#n!=1*2*....*n
#doble -> 1.8E308
#????n -> 171!
import sys
sys.set_int_max_str_digits(1000000000)

def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujmenych!")
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f"silnia z n={n} wynosi: {silnia(n)}")
except ValueError as ve:
    print(ve)
