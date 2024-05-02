def CriarUsuario(chave, nome=None, endereco=None, rg=None):
    
    while True:
        novoNome = input("Digite o nome do usuário: ")
        if nome == None:
            if (novoNome == ""):
                continue
            else:
                break
        else:
            if (novoNome == ""):
                novoNome = nome
        break
    
    while True:
        novoEndereco = input("Digite o endereço do usuário: ")
        if endereco == None:
            if (novoEndereco == ""):
                continue
            else:
                break
        else:
            if (novoEndereco == ""):
                novoEndereco = endereco
        break
    
    while True:
        novoRg = input("Digite o RG do usuário: ")
        if rg == None:
            if (novoRg == ""):
                continue
            else:
                break
        else:
            if (novoRg == ""):
                novoRg = rg
        break

    usuario = {
        "chave": chave,
        "nome": novoNome,
        "endereco": novoEndereco,
        "rg": novoRg
    }    
    
    return usuario
