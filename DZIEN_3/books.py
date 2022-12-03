class Book:
    #opis stanu -> konstruktor klasy
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()
        
    #opis zachowania -> funkcje klasy -> metody
    
    def create_book(self):
        print("utworzono nowy obiekt klasy Book")
        
    def print_book(self):
        print(f'książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł,'
              f'oprawa: {self.oprawa}.')
        
    def rabat(self):
        return 0.1*self.cena
