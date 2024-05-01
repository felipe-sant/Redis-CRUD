from database.connection import connection

def delete(chave):
  connection.delete(chave)
