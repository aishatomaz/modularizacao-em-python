from mini_biblioteca.livros import Livro
from mini_biblioteca.usuarios import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        if not livro.disponivel:
            raise ValueError(f"O livro '{livro.titulo}' já está emprestado!")
        
        self.livro = livro
        self.usuario = usuario
        self.ativo = True
        
        self.livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True
        print(f"Livro '{self.livro.titulo}' devolvido com sucesso.")