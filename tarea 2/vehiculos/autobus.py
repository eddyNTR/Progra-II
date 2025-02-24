from vehiculos.vehiculo import Vehiculo

# Clase derivada Autobus
class Autobus(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros):
        super().__init__(marca, modelo)
        self.capacidad_pasajeros = capacidad_pasajeros
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
    
    def conducir(self):
        print(f"Conduciendo el autobús {self.modelo}.")