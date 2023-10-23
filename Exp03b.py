# Nombre del archivo binario que vamos a crear
nombre_archivo = "mi_archivo.bin"

# Abrir el archivo en modo escritura binaria (si no existe, lo crea)
with open(nombre_archivo, "wb") as archivo:
    # Datos binarios que vamos a escribir en el archivo
    datos_binarios = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Escribir los datos binarios en el archivo
    archivo.write(datos_binarios)

print(f"Se ha creado el archivo binario '{nombre_archivo}' con los datos especificados.")
