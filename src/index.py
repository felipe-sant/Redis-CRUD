from menu.menuIndex import MenuIndex
from functions.cadastrarUsuario import CadastrarUsuario
from functions.listarUsuario import ListarUsuario
from functions.deletarUsuario import DeletarUsuario

from functions.deletarTodosUsuarios import DeletarTodosUsuarios

while True:
    MenuIndex()
    option = str(input("Digite a opção desejada: "))
    if option == "0":
        print("Saindo...")
        break
    elif option == "1":
        CadastrarUsuario()
    elif option == "2":
        ListarUsuario()
    elif option == "3":
        DeletarUsuario()
    elif option == "4":
        print("Deletar")
    elif option == "5":
        DeletarTodosUsuarios()
    else:
        print("Opção inválida")
