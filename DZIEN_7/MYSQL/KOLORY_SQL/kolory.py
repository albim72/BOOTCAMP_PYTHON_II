class Kolory:
    def __init__(self,nazwa_koloru,nazwa_palety):
        self.nazwa_koloru = nazwa_koloru
        self.nazwa_palety = nazwa_palety

    @property
    def nazwa_koloru(self):
        return self._nazwa_koloru

    @property
    def nazwa_palety(self):
        return self._nazwa_palety

    @nazwa_koloru.setter
    def nazwa_koloru(self,nazwa_koloru):
        self._nazwa_koloru = nazwa_koloru

    @nazwa_palety.setter
    def nazwa_palety(self, nazwa_palety):
        self._nazwa_palety = nazwa_palety
