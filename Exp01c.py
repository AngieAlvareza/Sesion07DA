# Función que recibe una lista y calcula la suma de sus elementos
def suma_elementos(lista):
    suma = sum(lista)
    return suma

# Función que recibe una tupla y encuentra el elemento máximo
def maximo_elemento(tupla):
    maximo = max(tupla)
    return maximo

mi_lista = [1, 2, 3, 4, 5]
mi_tupla = (10, 20, 30, 40, 50)

resultado_lista = suma_elementos(mi_lista)
resultado_tupla = maximo_elemento(mi_tupla)

print("Suma de elementos de la lista:", resultado_lista)
print("Máximo elemento de la tupla:", resultado_tupla)
