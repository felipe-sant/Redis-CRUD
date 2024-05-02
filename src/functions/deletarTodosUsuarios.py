from database.functions.keys import keys
from database.functions.delete import delete

def DeletarTodosUsuarios():
    chaves = keys("usuarios")

    for chave in chaves:
        delete(chave)
        print(f"Chave {chave} deletada com sucesso")
    
    print("\nTodos os usuários foram deletados com sucesso!\n")