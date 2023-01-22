from abstract_a import AbstractProductA

class ConcereteProduktA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "wynik: produkt A1"

class ConcereteProduktA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "wynik: produkt A2"
