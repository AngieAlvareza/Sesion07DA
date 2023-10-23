import sqlite3

# Conectar a la base de datos (o crear una nueva si no existe)
conn = sqlite3.connect('mi_basededatos.db')

# Crear un cursor para interactuar con la base de datos
cursor = conn.cursor()

# Aquí puedes ejecutar comandos SQL
# Por ejemplo, crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS estudiantes (
                  id INTEGER PRIMARY KEY,
                  nombre TEXT,
                  edad INTEGER,
                  curso TEXT,
                  matriculado INTEGER,
                  pago_pension INTEGER)''')



# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión
conn.close()
