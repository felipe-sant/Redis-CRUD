from database.functions.keys import keys
from database.functions.delete import delete

def DeletarTodosUsuarios():
    chaves = keys("usuarios")
    print(chaves)

    for chave in chaves:
        delete(chave)
        print(f"Chave {chave} deletada com sucesso")