# Función que recibe una lista y devuelve la suma y el promedio de sus elementos
def suma_y_promedio(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return suma, promedio

mi_lista = [1, 2, 3, 4, 5]

total, promedio = suma_y_promedio(mi_lista)

print("Suma de elementos:", total)
print("Promedio de elementos:", promedio)
