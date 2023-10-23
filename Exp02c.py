# Función que recibe un diccionario y devuelve la suma y el promedio de sus valores
def suma_y_promedio(diccionario):
    suma = sum(diccionario.values())
    promedio = suma / len(diccionario)
    return suma, promedio

mi_diccionario = {"a": 10, "b": 20, "c": 30, "d": 40}

total, promedio = suma_y_promedio(mi_diccionario)

print("Suma de valores:", total)
print("Promedio de valores:", promedio)
