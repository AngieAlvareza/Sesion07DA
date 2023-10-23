class Estudiante:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.curso = ""
        self.matriculado = False
        self.pago_pension = False

    def ingresarDatos(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.edad = int(input("Ingrese la edad del estudiante: "))
        self.curso = input("Ingrese el curso que está siguiendo: ")

    def imprimirDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Curso: {self.curso}")
        print(f"Matriculado: {'Sí' if self.matriculado else 'No'}")
        print(f"Pago de pensión: {'Sí' if self.pago_pension else 'No'}")

    def matricular(self):
        self.matriculado = True
        print(f"{self.nombre} se ha matriculado en {self.curso}.")

    def pagarPensión(self):
        if self.matriculado:
            self.pago_pension = True
            print(f"{self.nombre} ha pagado la pensión del curso {self.curso}.")
        else:
            print(f"{self.nombre} no puede pagar la pensión porque no está matriculado.")

    @staticmethod
    def obtener_info_importante():
        return "¡Estudiante importante!"

    @staticmethod
    def validar_nombre(nombre):
        return len(nombre) > 0

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
