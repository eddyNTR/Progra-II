from vehiculos.vehiculo import Vehiculo

# Clase derivada Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada}cc")
    
    def conducir(self):
        print(f"Conduciendo la motocicleta {self.modelo}.")