from abc import ABCMeta,abstractmethod


class IDane(metaclass=ABCMeta):

    @abstractmethod
    def opispojazdu(self):raise NotImplementedError

    @abstractmethod
    def silnik(self,rodzaj,poj,l_km):raise NotImplementedError
