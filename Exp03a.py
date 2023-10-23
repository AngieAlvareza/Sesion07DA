# Nombre del archivo que vamos a crear
nombre_archivo = "mi_archivo.txt"

# Abrir el archivo en modo escritura (si no existe, lo crea)
archivo = open(nombre_archivo, "w")

# Contenido que vamos a escribir en el archivo
contenido = "Hola, este es un archivo de texto creado con Python.\n"
contenido += "¡Espero que te sea útil para tus prácticas!\n"

# Escribir el contenido en el archivo
archivo.write(contenido)

# Cerrar el archivo
archivo.close()

print(f"Se ha creado el archivo '{nombre_archivo}' y se ha escrito el contenido en él.")
