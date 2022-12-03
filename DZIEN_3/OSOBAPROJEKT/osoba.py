class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.pracownik = False
        self.kolor_oczu = "brązowe"
        self.info()

    def info(self):
        print("utworzono nową osobę")

    def print_osoba(self):
        print(f'osoba -> imię: {self.imie}, wiek: {self.wiek}, wzrost: {self.wzrost} cm, '
              f'waga: {self.waga} kg, kolor oczu: {self.kolor_oczu}.')

    def wiek_za_x_lat(self,x):
        return self.wiek + x

    def czypracownik(self):
        return self.pracownik

    def setkolor(self,kolor):
        self.kolor_oczu = kolor
        
    def bmi(self):
        return self.waga/(self.wzrost/100)**2
    
    def opis_bmi(self):
        if self.bmi() <18.5:
            return "niedowaga"
        elif self.bmi()<=25:
            return "waga prawidłowa"
        elif self.bmi()<=30:
            return "nadwaga"
        else:
            return "otyłość"
