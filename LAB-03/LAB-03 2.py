from abc import ABC, abstractmethod
from typing import Any

class Padaria(ABC):
    
    @property
    @abstractmethod
    def Bolo(self) -> None:
        pass

    @abstractmethod
    def produzir_aniversario(self) -> None:
        pass

    @abstractmethod
    def produzir_casamento(self) -> None:
        pass

    @abstractmethod
    def produzir_festainformal(self) -> None:
        pass

class ConcretePadaria(Padaria):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Bolo()


class BoloChocolate():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

class BoloMandioca():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

class BoloCenoura():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)


class Director:
    def __init__(self) -> None:
        self._Padaria = None

    @property
    def Padaria(self) -> Padaria:
        return self._Padaria

    @Padaria.setter
    def Padaria(self, builder: Padaria) -> None:
        self._Padaria = Padaria

    def build_full_featured_product(self) -> None:
        self.Padaria.produzir_bolo_chocolate()
        self.Padaria.produzir_bolo_mandioca()
        self.Padaria.produzir_bolo_cenoura()


if __name__ == "__main__":
    Padaria.produce_part_a()
    Padaria.produce_part_b()
    Padaria.product.list_parts()

