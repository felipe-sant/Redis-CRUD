from database.connection import connection

def get(chave):
  return connection.get(chave)
