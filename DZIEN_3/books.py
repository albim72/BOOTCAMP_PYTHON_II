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

    def setcena(self,nowacena):
        self.cena = nowacena


print("_____ książka _______")
b1 = Book(23,"Wiedźmin","Andrzej Sapkowski",38)
b1.setcena(44)
b1.print_book()
print(f'standardowy rabat: {b1.rabat():.2f} zł')
print(f'kwota do zapłaty: {b1.cena - b1.rabat():.2f} zł')

print("_____ książka _______")
b2 = Book(57,"Hobbit","J.R.R. Tolkien",34)
b2.oprawa = "twarda"
b2.print_book()
print(f'standardowy rabat: {b2.rabat():.2f} zł')
print(f'kwota do zapłaty: {b2.cena - b2.rabat():.2f} zł')
