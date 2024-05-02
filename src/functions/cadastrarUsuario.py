from database.functions.set import set
from functions.criarChave import CriarChave
from functions.criarUsuario import CriarUsuario
from functions.verificarChaveExistente import VerificarChaveExistente
import json

def CadastrarUsuario():
    try:
        chave = CriarChave("usuarios")
        if (VerificarChaveExistente(chave)):
            raise Exception("Chave já existente!")
        else:
            usuario = CriarUsuario(chave)
            set(chave, json.dumps(usuario))
            print("\nUsuário cadastrado com sucesso!\n")
    except Exception as e:
        print(f"\nErro ao cadastrar usuário: {e}")
        input()
