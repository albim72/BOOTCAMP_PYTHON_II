from czlonekrodu import CzlonekRodu

class Tywin(CzlonekRodu):

    def walka(self):
        if self.punkty_walki > self.punkty_walki:
            print("Lord wysłany na pole walki....")
        else:
            print("Lord pozostaje w pałacu...")

    def negocjacja(self):
        if self.punkty_palacowe >=8 and self.punkty_walki < self.punkty_palacowe:
            print("Lord wysłany do negocjacji...")
        else:
            print("Lord wysłany do walki...")

    def uczta(self):
        pass
