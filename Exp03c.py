nombre_archivo = "archivo.txt"

# Abrir el archivo en modo escritura de texto (si no existe, lo crea; si existe, sobrescribe su contenido)
with open(nombre_archivo, "w") as archivo:
    # Escribir datos en el archivo
    archivo.write("Este es un ejemplo de escritura en un archivo de texto.\n")

print(f"Se ha escrito en el archivo de texto '{nombre_archivo}'.")
