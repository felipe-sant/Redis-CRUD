from database.functions.delete import delete
from functions.criarChave import CriarChave
from functions.buscarDados import BuscarDados

def DeletarUsuario():
    listaUsuarios = BuscarDados("usuarios")
    
    chaveParaExclusao = CriarChave("usuarios")
    
    for usuario in listaUsuarios:
        if usuario["chave"] == chaveParaExclusao:
            delete(chaveParaExclusao)
            print("Usuário deletado com sucesso")
            return