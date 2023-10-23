import sqlite3

# Crear una base de datos en un archivo
conn = sqlite3.connect('pedidos.db')

# Crear una base de datos en memoria (útil para pruebas)
# conn = sqlite3.connect(':memory:')

# Crear un objeto de cursor
cur = conn.cursor()

# Ejecutar una consulta SQL
cur.execute("CREATE TABLE pedidos (id INTEGER PRIMARY KEY, producto TEXT, cantidad INTEGER)")

# Consulta de ejemplo para insertar datos
producto = "Widget"
cantidad = 100
cur.execute("INSERT INTO pedidos (producto, cantidad) VALUES (?, ?)", (producto, cantidad))

# Guardar los cambios en la base de datos
conn.commit()

# Consulta para recuperar datos
cur.execute("SELECT * FROM pedidos")
rows = cur.fetchall()

# Imprimir resultados
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
