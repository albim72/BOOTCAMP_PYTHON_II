from abstract import AbstractFactory
from abstract_a import AbstractProductA
from abstract_b import AbstractProductB
from conc_prodA import ConcereteProduktA1, ConcereteProduktA2
from conc_prodB import ConcreteProductB1, ConcreteProductB2

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcereteProduktA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
    
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcereteProduktA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
