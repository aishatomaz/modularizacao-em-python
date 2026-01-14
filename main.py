from emprestimos import Emprestimo
from livros import Livros
from usuario import Usuarios
from emprestimos import Emprestismo

def executar():
    user = Usuarios("Clara", "U001")
    book = Livros("O Hobbit", "Daniel Golleman", "L001")
    
    print(f"--- Início ---\n{user}\n{book}\n")

    try:
        print(f"Realizando empréstimo para {user.nome}...")
        emp = Emprestimo(book, user)
        print(book) 
        
        print("\n / Devolução /")
        emp.devolver()
        print(book)
        
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    executar()