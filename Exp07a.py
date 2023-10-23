class Estudiante:
    def __init__(self):
        self._nombre = ""
        self._edad = 0
        self._curso = ""
        self._matriculado = False
        self._pago_pension = False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso

    @property
    def matriculado(self):
        return self._matriculado

    @property
    def pago_pension(self):
        return self._pago_pension

    def ingresarDatos(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")



