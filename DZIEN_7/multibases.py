class MultiBases(type):
    def __new__(cls, clsname, bases, clsdict):
        if len(bases) > 1:
            raise TypeError("Tylko jednodziedziczenie jest dopuszczalne dla tej klasy!")
        return super().__new__(cls, clsname, bases, clsdict)

class Base(metaclass=MultiBases):pass

class Pierwsza(Base):pass
class Druga(Pierwsza):pass

class Trzecia:pass

#class DKlasa(Pierwsza, Druga):pass
class DKlasa(Pierwsza, Trzecia):pass
