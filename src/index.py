from database.functions.delete import delete
from database.functions.set import set
from database.functions.get import get
from functions.print_decode import print_decode

print("Começando aplicação")

set("nome", "João")

print_decode(get("nome"))

delete("nome")

print_decode(get("nome"))
