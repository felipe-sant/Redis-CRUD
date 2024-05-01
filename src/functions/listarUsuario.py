from database.functions.keys import keys
from database.functions.get import get
import json

def ListarUsuario():
    chaves = keys("usuarios")
    
    if chaves:
        for chave in chaves:
            usuario = get(chave)
            print(json.loads(usuario))
    else:
        print("\nNenhum usuário cadastrado\n")
