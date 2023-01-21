import mysql.connector
from insertdata import dodawanie
from selectdata import pokaz
from filtr import filtr
from  kolory import Kolory


nk = input("podaj nazwę koloru: ")
pk = input("podaj nazwę palety: ")

kol = Kolory(nk,pk)
dodawanie(kol.nazwa_koloru,kol.nazwa_palety)

print("____________________________")
pokaz()

print("____________________________")

pal = input("podaj nazwę palety, aby wyfiltrować dane: ")
filtr(pal)
