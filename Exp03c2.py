nombre_archivo = "archivo.bin"

# Abrir el archivo en modo escritura binaria (si no existe, lo crea; si existe, sobrescribe su contenido)
with open(nombre_archivo, "wb") as archivo:
    # Datos binarios que vamos a escribir en el archivo
    datos_binarios = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Escribir los datos binarios en el archivo
    archivo.write(datos_binarios)

print(f"Se ha escrito en el archivo binario '{nombre_archivo}'.")
