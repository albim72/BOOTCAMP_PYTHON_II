from abc import ABC,abstractmethod


class Prototyp(ABC):
    def __init__(self,x):
        self.x = x

    def message(self):
        print("metoda nieabstrakcyjna klasy abstrakcyjnej")

    @abstractmethod
    def policz(self):
        pass

    #metoda abstrakcyjna z ciałem domyślnym
    @abstractmethod
    def policz_x(self):
        return self.x*7


class MojaKlasa(Prototyp):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return 455

    def policz_x(self):
        return super().policz_x() + self.y*2


mk = MojaKlasa(6,3)
print(f'wynik policz() -> {mk.policz()}')
print(f'wynik policz_x() -> {mk.policz_x()}')



