from platos.plato import Plato

class Pique(Plato):
    def __init__(self, nombre, precio, tamanio):
        super().__init__(nombre, precio)
        self.tamanio = tamanio
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"tamaño: {self.tamanio}")

    def entregar_plato(self):
        super().entregar_plato()
    
    def recojer_plato(self):
        super().recojer_plato()