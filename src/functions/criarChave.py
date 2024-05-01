def criarChave(colecao):
    while True:
        chave = input("Digite a chave: ")
        if chave == "":
            print("Chave inválida")
            continue
        break
    chave = colecao + "@" + chave.replace(" ", "_")
    return chave