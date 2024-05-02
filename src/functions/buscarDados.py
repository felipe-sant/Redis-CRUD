from database.functions.keys import keys
from database.functions.get import get
import json

def BuscarDados(tipo):
    chaves = keys(tipo)
    
    listaDados = []
    
    for chave in chaves:
        dado = get(chave)
        dado = json.loads(dado.decode("utf-8"))
        listaDados.append(dado)
        
    return listaDados