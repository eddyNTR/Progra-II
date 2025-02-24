from platos.plato import Plato

class Chicharon(Plato):
    def __init__(self, nombre, precio, tocino):
        super().__init__(nombre, precio)
        self.tocino = tocino

    def mostrar_info(self):
        super().mostrar_info()
        if self.tocino == "si":
            print("Con tocino")
        elif self.tocino == "no":
            print("Sin tocino")
        else:
            print("No se especifico si lleva tocino")
    
    def entregar_plato(self):
        return super().entregar_plato()
    
    def recojer_plato(self):
        return super().recojer_plato()
    
