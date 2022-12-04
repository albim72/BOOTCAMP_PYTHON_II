class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key = key
        self.value = value


    def __str__(self):
        return f"klucze i wartości muszą być listą lub krotką, aktualnie klucz {self.key} " \
               f"jest typem : {type(self.key)}, aktuanie wartości {self.value}  jest typem: {type(self.value)}"
