from database.functions.set import set
from functions.criarChave import criarChave
from functions.criarUsuario import CriarUsuario
import json

def CadastrarUsuario():
    chave = criarChave("usuarios")
    usuario = CriarUsuario()
    set(chave, json.dumps(usuario))