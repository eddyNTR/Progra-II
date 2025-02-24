from platos.plato import Plato

class Charque(Plato):
    def __init__(self, nombre, precio, extras):
        super().__init__(nombre, precio)
        self.extras = extras
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f"extras: {self.extras}")
    
    def entregar_plato(self):
        super().entregar_plato()
    
    def recojer_plato(self):
        super().recojer_plato()