class Opis:
    def __init__(self,string):
        self.string = string

    def __repr__(self):
        return f'Obiekt {self.string}'

    def __add__(self, other):
        return self.string + other


st = Opis('zimowa pogoda')
print(st + ' i mocny wiatr')
print(st + str(4500))

