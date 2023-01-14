from dataclasses import dataclass, astuple, asdict, field

@dataclass(order=True)
class Person:
    firstname:str = "Jan"
    lastname:str = "Nowak"
    age:int = 30
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)
    sort_index:int = field(init=False,repr=False)

    def __repr__(self):
        return f'Pracownik: {self.firstname} {self.lastname}, Stanowisko: {self.job}.'

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname
        self.sort_index = self.age


janek = Person()
print(janek)

print(astuple(janek))
print(asdict(janek))

print(janek.full_name)

aga = Person("Aga","Kot",21)
print(janek>aga)
