# Función que recibe un diccionario y encuentra el valor máximo
def maximo_valor(diccionario):
    max_valor = max(diccionario.values())
    return max_valor

# Función que recibe un diccionario y calcula la suma de los valores
def suma_valores(diccionario):
    suma = sum(diccionario.values())
    return suma

mi_diccionario = {"a": 10, "b": 20, "c": 30, "d": 40}

resultado_max = maximo_valor(mi_diccionario)
resultado_suma = suma_valores(mi_diccionario)

print("Máximo valor del diccionario:", resultado_max)
print("Suma de valores del diccionario:", resultado_suma)
