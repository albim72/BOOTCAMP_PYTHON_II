class IntFloatValueEror(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return f"wartość: {self.value} jest niewłaściwa. " \
               f"Słownik akceptuje tylko wartości typu int i float"
