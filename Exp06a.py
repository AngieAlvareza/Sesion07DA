class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def ingresarDatos(self):
        self.nombre = input("Nombre: ")
        self.edad = input("Edad: ")
        self.curso = input("Curso: ")

    def imprimirDatos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Curso:", self.curso)

estudiante = Estudiante("Juan", 20, "Matemáticas")
estudiante.ingresarDatos()
estudiante.imprimirDatos()
