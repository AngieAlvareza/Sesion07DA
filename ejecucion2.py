from estudiante import Estudiante

# Crear objetos de instancia de Estudiante y almacenarlos en una lista
estudiante1 = Estudiante("Estudiante1", 20, "Curso1")
estudiante2 = Estudiante("Estudiante2", 22, "Curso2")
estudiante3 = Estudiante("Estudiante3", 21, "Curso1")

lista_estudiantes = [estudiante1, estudiante2, estudiante3]


for estudiante in lista_estudiantes:
    estudiante.matricular()
