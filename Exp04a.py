# Nombre del archivo a crear
nombre_archivo = "mi_archivo.txt"

# Abrir el archivo en modo de escritura de texto ("w" para write)
with open(nombre_archivo, "w") as archivo:
    # Definir un bucle para escribir varias líneas
    while True:
        linea = input("Ingresa una línea de texto (o escribe 'fin' para terminar): ")
        if linea.lower() == 'fin':
            break
        archivo.write(linea + '\n')

print(f"Se han escrito las líneas en el archivo: {nombre_archivo}")
