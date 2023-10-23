import sqlite3
conn = sqlite3.connect('orders.db')

moreOrders = [(6, '03/10/2021', 3, 2015478), (7, '02/01/2019', 3, 2015698)]
conn.commit()