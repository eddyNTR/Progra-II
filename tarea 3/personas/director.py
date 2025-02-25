from personas.persona import Persona

class Director(Persona):
    def __init__(self, nombre, edad, ocupacion, genero, direccion, estado_civil, turno):
        super().__init__(nombre, edad, ocupacion, genero, direccion)
        self.estado_civil = estado_civil
        self.turno = turno

    def presentacion(self):
        super().presentacion()
        print(f"Mi estado civil es {self.estado_civil} y trabajo en el turno {self.turno}.")
    
    def saludar(self):
        super().saludar()
    
    def asistencia(self):
        super().asistencia()
    
    def tomar_decisiones(self):
        print(f"Estoy tomando decisiones.")
    
    def administrar(self):
        print(f"Estoy administrando la escuela.")
    
    def decomisar(self):
        print(f"Estoy decomisando objetos prohibidos.")
    

    
