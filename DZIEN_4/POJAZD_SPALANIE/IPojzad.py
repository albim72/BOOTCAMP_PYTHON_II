from abc import ABCMeta,abstractmethod

class IPojazd(metaclass=ABCMeta):
    @abstractmethod
    def spalanie_100(self,odl,litry):raise NotImplementedError

    @abstractmethod
    def koszt_przejazdu(self,odl,litry,cena_l):raise NotImplementedError

