import sqlite3

conn = sqlite3.connect('orders.db')
print("Base de datos abierta satisfactoriamente")
cur = conn.cursor()

# Consulta SQL con formato corregido
query = """
SELECT *, users.fname, users.lname
FROM orders
LEFT JOIN users ON users.userid = orders.userid;
"""

cur.execute(query)
result = cur.fetchall()

for row in result:
    print(row)

print("Consulta realizada satisfactoriamente")
conn.close()
