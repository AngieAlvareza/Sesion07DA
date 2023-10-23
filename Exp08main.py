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

    # Ejecutar los métodos estáticos
    info_importante = Estudiante.obtener_info_importante()
    print(info_importante)

    nombre_estudiante = estudiante.nombre
    es_nombre_valido = Estudiante.validar_nombre(nombre_estudiante)
    print(f"¿El nombre es válido? {'Sí' if es_nombre_valido else 'No'}")
