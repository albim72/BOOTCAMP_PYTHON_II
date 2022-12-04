from czlonekrodu import CzlonekRodu

class Cersei(CzlonekRodu):

    def walka(self):
        if self.punkty_walki>=7:
            print("Królowa wysłana na pole walki....")
        else:
            print("Królowa pozostaje w pałacu...")

    def negocjacja(self):
        if self.punkty_palacowe >= 8:
            print("Królowa wysłana do negocjacji...")
        else:
            print("Królowa zostaje w pałacu...")

    def uczta(self):
        if self.punkty_palacowe >=5 and self.doswiadczenie >=6:
            print("Królowa udaje się na ucztę...")
        else:
            print("Królowa zostaje w pałacu...")
