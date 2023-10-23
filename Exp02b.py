# Función que recibe un diccionario y una clave (con valor por defecto)
def obtener_valor(diccionario, clave="a"):
    valor = diccionario.get(clave, "Clave no encontrada")
    return valor

mi_diccionario = {"a": 10, "b": 20, "c": 30, "d": 40}

valor_a = obtener_valor(mi_diccionario)  # Obtiene el valor de la clave "a"
valor_x = obtener_valor(mi_diccionario, "x")  # Obtiene el valor de una clave que no existe

print("Valor de clave 'a':", valor_a)
print("Valor de clave 'x':", valor_x)
