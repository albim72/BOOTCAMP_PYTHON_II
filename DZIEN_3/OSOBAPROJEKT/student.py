from pracownik import Pracownik
from sport import Sport
from ekstra import Ekstra

class Student(Pracownik,Sport,Ekstra):
    #konstruktor z wielodziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,nrstudenta,wydzial,kierunek,rokstud,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dysycyplina="",lataupr="",zyciowka=""):
        Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dysycyplina,lataupr,zyciowka)
        self.nrstudenta = nrstudenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rokstud = rokstud
        
    def print_student(self):
        print(f'student {self.nrstudenta}, wydział: {self.wydzial}, kierunek: {self.kierunek},'
              f'rok studiów: {self.rokstud}.')

    def czypracownik(self):
        return self.firma != ""
