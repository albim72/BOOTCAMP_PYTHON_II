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
        
    def policz_ppm(self,plec):
        if plec == "k":
            return 655.1 + 9.563*self.waga +1.85*self.wzrost - 4.676*self.wiek
        elif plec == "m":
            return 66.5 + 13.75 * self.waga + 5.003 * self.wzrost - 6.775 * self.wiek
        else:
            return "nie ma takiego wyboru, wybierz k lub m"
        
