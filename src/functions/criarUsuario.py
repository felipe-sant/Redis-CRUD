def CriarUsuario():
    while True:
        nome = input("Digite o nome do usuário: ")
        if nome == "":
            print("Nome inválido")
            continue
        break
    
    while True:
        endereco = input("Digite o endereço do usuário: ")
        if endereco == "":
            print("Endereço inválido")
            continue
        break

    while True:
        rg = input("Digite o RG do usuário: ")
        if rg == "":
            print("RG inválido")
            continue
        break
    
    usuario = {
        "nome": nome,
        "endereco": endereco,
        "rg": rg
    }    
    
    return usuario
