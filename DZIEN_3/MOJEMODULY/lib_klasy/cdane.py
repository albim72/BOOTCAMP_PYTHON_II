from lib_funkcje.bfunkcje import *

class CDane:
    def __init__(self,lista,slownik):
        self.slownik = slownik
        self.lista = lista
        
    def czytaj_l(self):
        return czytaj_liste(self.lista)
    
    def czytaj_d(self):
        return czytaj_dict(self.slownik)
