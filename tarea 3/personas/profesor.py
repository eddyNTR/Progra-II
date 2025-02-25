from personas.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, ocupacion, genero, direccion, grado, materia, salario, turno):
        super().__init__(nombre, edad, ocupacion, genero, direccion)
        self.grado = grado
        self.materia = materia
        self.salario = salario
        self.turno = turno

    def presentacion(self):
        super().presentacion()
        print(f"Soy profesor de {self.materia} tengo un grado de {self.grado} doy clases en el turno {self.turno} y mi salario es de {self.salario}.")
    
    def saludar(self):
        super().saludar()
    
    def evaluar(self):
        print(f"Estoy tomando examen a los estudiantes.")
    
    def asistencia(self):
        super().asistencia()
    
    def tomar_lista(self):
        print(f"Estoy tomando lista a los estudiantes.")
    
    def educar(self):
        print(f"Estoy educando a los estudiantes.")