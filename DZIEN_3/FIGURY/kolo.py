import math

from figura import Figura

#utwórz klasę Kolo(Figura) i wyznacz pole koła oraz opisz konstruktor, a następnie w main() policz pole koła dla
#promienia = 5.5
#polekola = pi*a**2 -> math.pi

class Kolo(Figura):
    def __init__(self,a):
        super().__init__(a,0)

    def policz_pole(self):
        return math.pi*self.a**2
