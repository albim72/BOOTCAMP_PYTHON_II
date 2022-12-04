class UnaryOperator(object):
    def __init__(self,value):
        self.value = value

    def __pos__(self):
        print('metoda magiczna __pos__')
        return (+self.value)

    def __neg__(self):
        print('metoda magiczna __neg__')
        return (-self.value)

up = UnaryOperator(90)
print(+up)
print(-up)
