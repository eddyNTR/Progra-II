from personas.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, ocupacion, genero, direccion, grado, matricula, iq):
        super().__init__(nombre, edad, ocupacion, genero, direccion)
        self.grado = grado
        self.matricula = matricula
        self.iq = iq
    
    def presentacion(self):
        super().presentacion()
        print(f"Estudio en el grado {self.grado}, mi matricula es {self.matricula} tengo un IQ de {self.iq}.")
    
    def saludar(self):
        super().saludar()
        print(f"Soy estudiante.")
    
    def asistencia(self):
        super().asistencia()

    def estudiar(self):
        print(f"Estoy estudiando programacion.")
    
    def hacer_tarea(self):
        print(f"Estoy haciendo la tarea de programacion")
    
    def aprobar(self):
        print(f"Aprobe programacion.")
