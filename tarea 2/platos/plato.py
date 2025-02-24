class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"plato: {self.nombre}")
        print(f"precio: {self.precio} Bs")

    def entregar_plato(self):
        print(f"Plato {self.nombre}: entregado")

    def recojer_plato(self):
        print(f"Plato {self.nombre}: recogido")