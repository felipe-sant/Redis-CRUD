from database.functions.keys import keys
from database.functions.get import get
import json

def ListarUsuario():
    print()
    chaves = keys("usuarios")
    if chaves:
        for chave in chaves:
            usuario = get(chave)
            usuario = json.loads(usuario.decode("utf-8"))
            
            chave = chave.decode("utf-8")
            nome = usuario["nome"]
            endereco = usuario["endereco"]
            rg = usuario["rg"]
            
            print("Chave:", chave.replace("usuarios@", ""))
            print("Nome:", nome)
            print("Endereço:", endereco)
            print("RG:", rg)
            input()
    else:
        print("Nenhum usuário cadastrado\n")
