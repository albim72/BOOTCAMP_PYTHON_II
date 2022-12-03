class Pierwsza:
    def __init__(self,a):
        self.a = a

    def policz(self):
        return self.a*9

class Druga(Pierwsza):
    def __init__(self,a,b):
        Pierwsza.__init__(self,a)
        self.b = b

class CzterdziestaCzwarta:
    def __init__(self,n):
        self.n = n


class Trzecia(Druga,CzterdziestaCzwarta):
    def __init__(self,a,b,n):
        Druga.__init__(self, a, b)
        CzterdziestaCzwarta.__init__(self,n)

    def policz(self):
        return super().policz() + self.n*2

tr = Trzecia(3,5.5,0.0987)
print(f'wynik = {tr.policz()}')

print(issubclass(Trzecia,Druga))
print(issubclass(Trzecia,CzterdziestaCzwarta))
print(issubclass(Trzecia,Pierwsza))

print(issubclass(Pierwsza,Druga))
print(isinstance(Pierwsza,Druga))
print(issubclass(CzterdziestaCzwarta,Trzecia))
