class Component:

    def __init__(self):
        print('obiekt klasy Component został utworzony! ')

    def m1(self):
        print('metoda m1() została wykonana!')


class Composite:

    def __init__(self):
        self.obj1 = Component()
        print('obiekt klasy Composite został utworzony!')

    def m2(self):
        print('Metoda m2() klasy Composite została wykonana...')
        self.obj1.m1()

obj2 = Composite()
obj2.m2()

