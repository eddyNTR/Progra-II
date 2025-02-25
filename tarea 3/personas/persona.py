class Persona:
    def __init__(self, nombre, edad, ocupacion, genero, direccion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        self.genero = genero
        self.direccion = direccion
    
    def presentacion(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.ocupacion} y vivo en {self.direccion}.")
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
    
    def asistencia(self):
        print(f"Estoy presente.")