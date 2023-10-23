def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def ingresar_numero():
    numero = int(input("Ingresa un número (o 0 para salir): "))
    return numero

def menu():
    while True:
        print("Menú de opciones:")
        print("1. Determinar si un número es primo.")
        print("0. Salir.")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            numero = ingresar_numero()
            if numero == 0:
                break
            if es_primo(numero):
                print(f"{numero} es primo.")
            else:
                print(f"{numero} no es primo.")
        elif opcion == 0:
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
