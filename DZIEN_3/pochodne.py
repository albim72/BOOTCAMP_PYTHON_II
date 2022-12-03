class Base(object):
    def __init__(self,name):
        self.name = name

    def getname(self):
        return self.name


class Child(Base):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def getage(self):
        return self.age

class GrandChild(Child):
    def __init__(self,name,age,city):
        super().__init__(name,age)
        self.city = city

    def getcity(self):
        return self.city


osoba = GrandChild("Bonifacy",19,"Kraków")
print(f'student: {osoba.getname()}, wiek: {osoba.getage()}, miasto: {osoba.getcity()}.')

