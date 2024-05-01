from database.connection import connection

def keys(chave):
    return connection.keys(chave+"@*")
