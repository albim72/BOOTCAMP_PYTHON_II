from datetime import date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def ile_od_narodzin(cls,name,year):
        return cls(name,date.today().year - year)

    @staticmethod
    def czydorosly(age):
        return age >= 18

pr1 = Person('Roman',40)
pr2 = Person.ile_od_narodzin('Anna',1981)

print(pr1)
print(type(pr1))
print(pr2)
print(type(pr2))

print(pr1.age)
print(pr2.age)

print(Person.czydorosly(67))
print(pr1.czydorosly(pr1.age))

print(pr1==pr2)

pr3 = Person.ile_od_narodzin('Olaf',1991)
pr4 = Person.ile_od_narodzin('Hanna',1970)

print(pr3==pr4)
print(pr3)
print(pr4)


