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
        estudiante.pagarPensión()
    
    estudiante.imprimirDatos()

    # Ejecutar los métodos de clase
    descripcion = Estudiante.obtener_descripcion_estudiante(estudiante.nombre, estudiante.edad, estudiante.curso)
    print(descripcion)

    edad_estudiante = estudiante.edad
    jubilado = Estudiante.verificar_jubilación(edad_estudiante)
    print(f"¿Está jubilado? {'Sí' if jubilado else 'No'}")
