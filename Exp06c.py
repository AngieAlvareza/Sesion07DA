from estudiante import Estudiante

if __name__ == "__main__":
    estudiante = Estudiante()
    estudiante.ingresarDatos()
    estudiante.imprimirDatos()

    opcion = input("¿Desea matricular al estudiante? (Sí/No): ").lower()
    if opcion == "sí":
        estudiante.matricular()
    
    opcion = input("¿Desea pagar la pensión? (Sí/No): ").lower()
    if opcion == "sí":
        estudiante.pagarPension()
    
    estudiante.imprimirDatos()