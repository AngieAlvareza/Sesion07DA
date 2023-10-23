from estudiante import Estudiante
from menu import menu

if __name__ == "__main__":
    estudiante1 = Estudiante()
    estudiante2 = Estudiante()

    # Configurar datos para el estudiante1
    estudiante1.ingresarDatos()
    estudiante1.matricular()

    # Configurar datos para el estudiante2
    estudiante2.ingresarDatos()
    estudiante2.matricular()

    # Ejecutar el menú para interactuar con los estudiantes
    menu()
