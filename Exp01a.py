# Crear una lista para almacenar los números ingresados
numeros = [1,2,3]

# Usar un ciclo para capturar los 6 números uno a uno
for i in range(6):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i + 1}: "))
            if numero not in numeros:
                numeros.append(numero)
                break
            else:
                print("El número ya fue ingresado. Ingrese un número diferente.")
        except ValueError:
            print("Ingrese un número válido.")

# Mostrar los números ingresados
print("Números ingresados:")
for numero in numeros:
    print(numero)


# Encontrar el número más grande
numero_maximo = max(numeros)

# Encontrar el número más pequeño
numero_minimo = min(numeros)

# Calcular el punto medio
punto_medio = sum(numeros) / len(numeros)

# Encontrar el número más cercano al punto medio
numero_cercano = min(numeros, key=lambda x: abs(x - punto_medio))

# Mostrar los resultados
print(f"Número más grande: {numero_maximo}")
print(f"Número más pequeño: {numero_minimo}")
print(f"Número más cercano al punto medio: {numero_cercano}")

