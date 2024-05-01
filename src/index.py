from database.functions.set import set
from database.functions.get import get
from database.functions.keys import keys
from functions.print_decode import print_decode
from functions.cadastrarUsuario import CadastrarUsuario
from functions.listarUsuario import ListarUsuario
from menu.menuIndex import MenuIndex

while True:
    MenuIndex()
    option = str(input("Digite a opção desejada: "))
    if option == "0":
        print_decode("Saindo...")
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
        print_decode("Opção inválida")
