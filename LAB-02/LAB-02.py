class Operacoes:

    def AdicionarLivro (self) -> None:
        print('O livro {} foi adicionado'. format(nome))

    def RemoverLivro (self) -> None:
        print('O livro {} foi removido'. format(nome))


    def CadastrarAutor (self, nome: str, email: str, titpubli: str) -> None:
        if isinstance(nome, str) and isinstance(email, str) and isinstance(titpubli, str):
            print('Cadastrar o autor {}, e-mail {} e titulos publicados: {}'. format(nome, email, titpubli))
        else:
            self.IndicarErro() 
      
    def CadastrarCliente (self, nome: str, email: str, compra: str) -> None:
        if isinstance(nome, str) and isinstance(email, str) and isinstance(compra, str):
            print('Cadastrar o cliente {}, e-mail {} e compras passadas: {}'. format(nome, email, compra))
        else:
           self.IndicarErro() 
    
    def IndicarErro (self) -> None:
        print('Dados invalidos!')


class Livro:
    def __init__(self, titulo, autor, genero, edicao, precovenda, precocompra, imposto):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.edicao = edicao
        self.precovenda = precovenda
        self.precocompra = precocompra
        self.imposto = imposto

class Cliente:
    def __init__(nome, email, compra):
        self.nome = nome
        self.email = email
        self.compra = compra

class Autor:
    def __init__(nome, email, titpubli):
        self.nome = nome
        self.email = email
        self.titpubli = titpubli




        
