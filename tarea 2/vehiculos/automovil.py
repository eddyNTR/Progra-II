from vehiculos.vehiculo import Vehiculo
# Clase derivada Automovil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)
        self.tipo_motor = tipo_motor
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tipo de motor: {self.tipo_motor}")
    
    def conducir(self):
        print(f"Conduciendo el automóvil {self.modelo}.")
