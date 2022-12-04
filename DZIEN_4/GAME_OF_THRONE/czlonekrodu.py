from abc import ABC,abstractmethod

class CzlonekRodu(ABC):
    def __init__(self,nazwa_rodu,tytul,plec,punkty_walki,punkty_palacowe,doswiadczenie):
        self.tytul = tytul
        self.nazwa_rodu = nazwa_rodu
        self.plec = plec
        self.punkty_walki = punkty_walki
        self.punkty_palacowe = punkty_palacowe
        self.doswiadczenie = doswiadczenie

    @abstractmethod
    def walka(self):
        pass

    @abstractmethod
    def negocjacja(self):
        pass

    @abstractmethod
    def uczta(self):
        pass

    def get_tytul(self):
        return self.tytul
