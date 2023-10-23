from estudiante import Estudiante

def menu():
    print("Bienvenido al sistema de estudiantes")
    estudiante = Estudiante()

    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar datos del estudiante")
        print("2. Imprimir datos del estudiante")
        print("3. Matricular al estudiante")
        print("4. Pagar la pensión")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            estudiante.ingresarDatos()
        elif opcion == "2":
            estudiante.imprimirDatos()
        elif opcion == "3":
            estudiante.matricular()
        elif opcion == "4":
            estudiante.pagarPension()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    menu()
