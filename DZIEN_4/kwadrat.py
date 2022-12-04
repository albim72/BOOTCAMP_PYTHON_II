class Kwadrat:
    def __init__(self,bok):
        self.bok = bok

    def pole(self):
        return self.bok**2

class Prostokat:
    def __new__(cls, width:float, height:float):
        if width == height:
            return Kwadrat(bok=width)
        return object.__new__(Prostokat)

    def __init__(self,width:float, height:float):
        self.width = width
        self.height = height

    def pole(self):
        return self.width*self.height

r1 = Prostokat(8.8,4)
r2 = Prostokat(4.5,4.5)

print(type(r1))
print(f"pole figury {r1.__class__.__name__} wynosi: {r1.pole()}")

print(type(r2))
print(f"pole figury {r2.__class__.__name__} wynosi: {r2.pole()}")


