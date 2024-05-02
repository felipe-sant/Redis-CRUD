from functions.buscarDados import BuscarDados

def VerificarChaveExistente(chave):
    listaUsuarios = BuscarDados("usuarios")
    for usuario in listaUsuarios:
        if usuario["chave"] == chave:
            return True
    return False