def buscar_reemplazar_texto(archivo, palabra_buscar, palabra_reemplazar):
    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as archivo_entrada:
        contenido = archivo_entrada.read()

    # Realizar la búsqueda y reemplazo
    contenido_modificado = contenido.replace(palabra_buscar, palabra_reemplazar)

    # Abrir el archivo en modo escritura y escribir el contenido modificado
    with open(archivo, 'w') as archivo_salida:
        archivo_salida.write(contenido_modificado)

if __name__ == "__main__":
    nombre_archivo = "abc.txt"  # Reemplaza con el nombre de tu archivo
    palabra_buscar = "texto_a_buscar"
    palabra_reemplazar = "texto_a_reemplazar"

    buscar_reemplazar_texto(nombre_archivo, palabra_buscar, palabra_reemplazar)

    print("Texto reemplazado con éxito.")
