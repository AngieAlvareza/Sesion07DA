# Función que recibe una lista y un valor para agregar al final (con valor por defecto)
def agregar_elemento(lista, elemento=0):
    lista.append(elemento)

mi_lista = [1, 2, 3]

agregar_elemento(mi_lista)  # Agrega 0 por defecto
agregar_elemento(mi_lista, 4)  # Agrega el valor especificado

print("Lista con elementos agregados:", mi_lista)
