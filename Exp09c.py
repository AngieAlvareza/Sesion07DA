import sqlite3

# Creamos una conexión a la base de datos (asegúrate de que el archivo de la base de datos exista)
conn = sqlite3.connect('orders.db')

# Creamos un objeto cursor
cur = conn.cursor()

# Creamos la tabla "users" si no existe
cur.execute("""CREATE TABLE IF NOT EXISTS users (
    userid INT PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT
);""")


cur.execute("""CREATE TABLE IF NOT EXISTS orders(
 orderid INT PRIMARY KEY,
 date TEXT,
 userid TEXT,
 total TEXT);
""")
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
for table in tables:
    print("Nombre de la tabla:", table[0])

conn.commit()

# Guardamos los cambios en la base de datos
conn.commit()

# Cerramos la conexión
conn.close()
