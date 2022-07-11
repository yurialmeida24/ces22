from abc import ABC, abstractmethod

class Padaria(ABC):

    @abstractmethod
    def criar_bolo_chocolate(self) -> AbstractBoloChocolate:
        pass


    @abstractmethod
    def criar_bolo_mandioca(self) -> AbstractBoloMandioca:
        pass


    @abstractmethod
    def criar_bolo_cenoura(self) -> AbstractBoloCenoura:
        pass

class Aniversario(Padaria):

    @abstractmethod
    def criar_bolo_chocolate(self) -> AbstractBoloChocolate:
        return AbstractBoloChocolate1()
        pass


    @abstractmethod
    def criar_bolo_mandioca(self) -> AbstractBoloMandioca:
        return AbstractBoloMandioca1()
        pass


    @abstractmethod
    def criar_bolo_cenoura(self) -> AbstractBoloCenoura:
        return AbstractBoloCenoura1()
        pass    

class Casamento(Padaria):

    @abstractmethod
    def criar_bolo_chocolate(self) -> AbstractBoloChocolate:
        return AbstractBoloChocolate2()
        pass


    @abstractmethod
    def criar_bolo_mandioca(self) -> AbstractBoloMandioca:
        return AbstractBoloMandioca2()
        pass


    @abstractmethod
    def criar_bolo_cenoura(self) -> AbstractBoloCenoura:
        return AbstractBoloCenoura2()
        pass 

class FestaInformal(Padaria):

    @abstractmethod
    def criar_bolo_chocolate(self) -> AbstractBoloChocolate:
        return AbstractBoloChocolate3()
        pass


    @abstractmethod
    def criar_bolo_mandioca(self) -> AbstractBoloMandioca:
        return AbstractBoloMandioca3()
        pass


    @abstractmethod
    def criar_bolo_cenoura(self) -> AbstractBoloCenoura:
        return AbstractBoloCenoura3()
        pass 


class AbstractBoloChocolate(ABC):

    @abstractmethod
    def tipoBolo(self) -> str:
        pass

class BoloChocolateAniversario(AbstractBoloChocolate):
    def tipoBolo(self) -> str:
        return "Bolo de chocolate com estilo aniversario."

class BoloChocolateCasamento(AbstractBoloChocolate):
    def tipoBolo(self) -> str:
        return "Bolo de chocolate com estilo casamento."

class BoloChocolateFestaInformal(AbstractBoloChocolate):
    def tipoBolo(self) -> str:
        return "Bolo de chocolate com estilo festa informal."


class AbstractBoloMandioca(ABC):

    @abstractmethod
    def tipoBolo(self) -> str:
        pass

class BoloMandiocaAniversario(AbstractBoloMandioca):
    def tipoBolo(self) -> str:
        return "Bolo de mandioca com estilo aniversario."

class BoloMandiocaCasamento(AbstractBoloMandioca):
    def tipoBolo(self) -> str:
        return "Bolo de mandioca com estilo casamento."

class BoloMandiocaFestaInformal(AbstractBoloMandioca):
    def tipoBolo(self) -> str:
        return "Bolo de mandioca com estilo festa informal."


class AbstractBoloCenoura(ABC):

    @abstractmethod
    def tipoBolo(self) -> str:
        pass

class BoloCenouraAniversario(AbstractBoloCenoura):
    def tipoBolo(self) -> str:
        return "Bolo de cenoura com estilo aniversario."

class BoloCenouraCasamento(AbstractBoloCenoura):
    def tipoBolo(self) -> str:
        return "Bolo de cenoura com estilo casamento."

class BoloCenouraFestaInformal(AbstractBoloCenoura):
    def tipoBolo(self) -> str:
        return "Bolo de cenoura com estilo festa informal."

def client(factory: Padaria) -> None:
    BoloChocolate = Padaria.criar_BoloChocolate()
    BoloMandioca = Padaria.criar_BoloMandioca()
    BoloCenoura = Padaria.criar_BoloCenoura()
 

