class A(object):

    def mojafunkcja(self):
        print("to jest moja funkcja klasy A")

class B(A):

    def mojafunkcja(self):
        print("to jest moja funkcja klasy B")
        super(B, self).mojafunkcja()

class C(B):

    def mojafunkcja(self):
        print("to jest moja funkcja klasy C")
        super(C, self).mojafunkcja()


ob = C()

ob.mojafunkcja()
