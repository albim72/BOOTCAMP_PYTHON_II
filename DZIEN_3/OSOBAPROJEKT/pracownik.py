from osoba import Osoba

class Pracownik(Osoba):
    #konstruktor z dziedziczeniem
    def __init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,wiek,waga,wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie
        self.pracownik = True
        
    def print_pracownik(self):
        print(f'pracownik -> firma: {self.firma},stanowisko pracy: {self.stanowisko}, '
              f'lata pracy: {self.latapracy}, wynagrodzenie miesięczne: {self.wynagrodzenie} zł')
        
