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

    
print(estudiante.nombre)  # Acceder al nombre
print(estudiante.edad)    # Acceder a la edad
print(estudiante.curso)   # Acceder al curso

estudiante.nombre = "Nuevo Nombre"  # Modificar el nombre
estudiante.edad = 25             # Modificar la edad
estudiante.curso = "Nuevo Curso"   # Modificar el curso
