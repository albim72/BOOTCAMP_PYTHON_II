class MojaMeta(type):

    def __new__(cls, nazwaklasy, dziedziczone, atrs):
        print(f"nazwa klasy: {nazwaklasy}")
        print(f"klasy dziedziczone: {dziedziczone}")
        print(f"zbiór atrybutów: {atrs}")
        return type.__new__(cls, nazwaklasy, dziedziczone, atrs)

    @property
    def empty(cls):
        return "pusto..."

class Zwykla:
    pass

class Base(Zwykla,metaclass=MojaMeta):
    pass

class Second(Base):
    pass

class Obok:
    pass

class Third(Obok,Base):
    pass


