import os

# Nombre del archivo que deseas verificar
nombre_archivo = "orders.txt"

# Verifica si el archivo existe
if os.path.isfile(nombre_archivo):
    print(f"El archivo '{nombre_archivo}' existe.")
else:
    print(f"El archivo '{nombre_archivo}' no existe.")
