import sqlite3

# Conectar a una base de datos SQLite existente o crear una nueva
conn = sqlite3.connect('ORDERS.db')

# Imprimir un mensaje si la conexión se realiza con éxito
print("Base de datos abierta satisfactoriamente")

# Cerrar la conexión a la base de datos cuando hayas terminado
conn.close()
