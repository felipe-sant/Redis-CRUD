from database.functions.get import get
from database.functions.set import set
from functions.criarChave import CriarChave
from functions.verificarChaveExistente import VerificarChaveExistente
from functions.criarUsuario import CriarUsuario
import json

def AtualizarUsuario():
    try:
        chaveParaAtualizar = CriarChave("usuarios")
        if (VerificarChaveExistente(chaveParaAtualizar)):
            usuario = get(chaveParaAtualizar)
            usuario = json.loads(usuario.decode("utf-8"))
            usuario = CriarUsuario(usuario["chave"], usuario["nome"], usuario["endereco"], usuario["rg"])
            set(chaveParaAtualizar, json.dumps(usuario))
            print("\nUsuário atualizado com sucesso!\n")
        else:
            raise Exception("Chave não encontrada!")
    except Exception as e:
        print(f"\nErro ao atualizar usuário: {e}")
        input()