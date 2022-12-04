from czlonekrodu import CzlonekRodu

class Tyrion(CzlonekRodu):

    def walka(self):
        if self.punkty_walki > self.punkty_walki and self.punkty_walki>=6:
            print("Lord wysłany na pole walki....")
        else:
            print("Lord pozostaje w pałacu...")

    def negocjacja(self):
        if self.punkty_palacowe >= 8:
            print("Lord wysłany do negocjacji...")
        else:
            print("Lord zostaje w pałacu...")

    def uczta(self):
        if self.punkty_palacowe >=6 and self.doswiadczenie >=7:
            print("Lord udaje się na ucztę...")
        else:
            print("Lord zostaje w pałacu...")
