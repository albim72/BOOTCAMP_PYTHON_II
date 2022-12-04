class InvertClass(object):

    def __init__(self,value):
        self._value = value

    def __invert__(self):
        return self._value[::-1]

    def __str__(self):
        return self._value

inv = InvertClass("Zielone Jabłuszko")
invValue = ~inv
print(invValue)
