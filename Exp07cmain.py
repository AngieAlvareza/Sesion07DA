from estudiante import Estudiante
if __name__ == "__main__":
    Exp07c = Estudiante()
    Exp07c.ingresarDatos()
    Exp07c.imprimirDatos()

    opcion = input("¿Desea matricular al estudiante? (Sí/No): ").lower()
    if opcion == "sí":
        Exp07c.matricular()
    
    opcion = input("¿Desea pagar la pensión? (Sí/No): ").lower()
    if opcion == "sí":
        Exp07c.pagarPensión()
    
    Exp07c.imprimirDatos()

    # Ejecutar los métodos estáticos
    info_importante = Exp07c.obtener_info_importante()
    print(info_importante)

    nombre_estudiante = estudiante.nombre
    es_nombre_valido = Estudiante.validar_nombre(nombre_estudiante)
    print(f"¿El nombre es válido? {'Sí' if es_nombre_valido else 'No'}")
