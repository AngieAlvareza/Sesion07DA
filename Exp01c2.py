# Función que recibe una lista y agrega un elemento al final
def agregar_elemento(lista, elemento):
    lista.append(elemento)

# Función que recibe una tupla y crea una lista a partir de ella
def tupla_a_lista(tupla):
    lista = list(tupla)
    return lista

mi_lista = [1, 2, 3]
mi_tupla = (4, 5, 6)
nuevo_elemento = 7

agregar_elemento(mi_lista, nuevo_elemento)
nueva_lista = tupla_a_lista(mi_tupla)

print("Lista con nuevo elemento:", mi_lista)
print("Tupla convertida a lista:", nueva_lista)
