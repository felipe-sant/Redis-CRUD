from functions.buscarDados import BuscarDados

def ListarUsuario():
    print()
    listaUsuarios = BuscarDados("usuarios")
    
    for usuario in listaUsuarios:
        chave = usuario["chave"]
        nome = usuario["nome"]
        endereco = usuario["endereco"]
        rg = usuario["rg"]
        print("Chave:", chave)
        print("Nome:", nome)
        print("Endereço:", endereco)
        print("RG:", rg)
        input()
