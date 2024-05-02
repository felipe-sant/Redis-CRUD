from database.functions.set import set
from functions.criarChave import CriarChave
from functions.criarUsuario import CriarUsuario
import json

def CadastrarUsuario():
    try:
        chave = CriarChave("usuarios", None)
        usuario = CriarUsuario(chave)
        set(chave, json.dumps(usuario))
    except Exception as e:
        print("\nErro ao cadastrar usuário\n")
        print(e)
