class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f"Plato: {self.nombre}")
        print(f"Precio: {self.precio}")

class Pique(Plato):
    def __init__(self, nombre, precio, tamanio):
        super().__init__(nombre, precio)
        self.tamanio = tamanio
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tamaño: {self.tamanio}")
    
    def entregar(self):
        print(f"Entregando {self.nombre}-{self.tamanio}")

class Charque(Plato):
    def __init__(self, nombre, precio, extras):
        super().__init__(nombre, precio)
        self.extras = extras
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Extras: {self.extras}")

    def recoger(self):
        print(f"Recogiendo {self.nombre}-{self.extras}")

charque = Charque("Charque", 25, "Papas fritas")
pique = Pique("Pique", 30, "Grande")

charque.mostrar_informacion()
charque.recoger()
print(" ")
pique.mostrar_informacion()
pique.entregar()