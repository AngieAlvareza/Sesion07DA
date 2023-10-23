def buscar_palabra_en_archivo(archivo, palabra_a_buscar):
    try:
        with open(archivo, 'r') as archivo_entrada:
            contenido = archivo_entrada.read()
            if palabra_a_buscar in contenido:
                return True
            else:
                return False
    except FileNotFoundError:
        return False

if __name__ == "__main__":
    nombre_archivo = "angie.txt"  # Reemplaza con el nombre de tu archivo
    palabra_a_buscar = "a"

    if buscar_palabra_en_archivo(nombre_archivo, palabra_a_buscar):
        print(f"La palabra '{palabra_a_buscar}' se encuentra en el archivo.")
    else:
        print(f"La palabra '{palabra_a_buscar}' no se encuentra en el archivo.")