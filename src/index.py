from functions.cadastrarUsuario import CadastrarUsuario
from functions.listarUsuario import ListarUsuario
from menu.menuIndex import MenuIndex

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
        print("Atualizar")
    elif option == "4":
        print("Deletar")
    else:
        print("Opção inválida")
