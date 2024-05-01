from database.connection import connection

def set(chave, valor):
  connection.set(chave, valor)
