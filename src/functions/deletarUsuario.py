from database.functions.delete import delete
from functions.criarChave import CriarChave
from functions.verificarChaveExistente import VerificarChaveExistente

def DeletarUsuario():
    try:
        chaveParaExcluir = CriarChave("usuarios")
        if (VerificarChaveExistente(chaveParaExcluir)):
            delete(chaveParaExcluir)
            print("\nUsuário deletado com sucesso!\n")
        else:
            raise Exception("Chave não encontrada!")
    except Exception as e:
        print(f"\nErro ao deletar usuário: {e}")
        input()
