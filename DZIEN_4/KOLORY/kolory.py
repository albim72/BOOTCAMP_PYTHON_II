class Kolor:

    #reprezentacja stanu -> konstruktor klasy
    def __init__(self,id,kolor,paleta):
        self._id = id
        self._kolor = kolor
        self._paleta = paleta

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def kolor(self):
        return self._kolor

    @id.setter
    def id(self, kolor):
        self._kolor = kolor

    @property
    def paleta(self):
        return self._paleta

    @paleta.setter
    def paleta(self, paleta):
        self._paleta = paleta

