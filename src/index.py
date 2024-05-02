from menu.menuIndex import MenuIndex
from functions.cadastrarUsuario import CadastrarUsuario
from functions.listarUsuario import ListarUsuario
from functions.atualizarUsuario import AtualizarUsuario
from functions.deletarUsuario import DeletarUsuario
from functions.deletarTodosUsuarios import DeletarTodosUsuarios

print("\nBem-vindo ao sistema de cadastro de usuários\n")

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
        AtualizarUsuario()
    elif option == "4":
        DeletarUsuario()
    elif option == "5":
        DeletarTodosUsuarios()
    else:
        print("\nOpção inválida\n")
