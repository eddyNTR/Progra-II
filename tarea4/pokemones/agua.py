from pokemones.pokemon import Pokemon

class Agua(Pokemon):
    def __init__(self, num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo, ):
        super().__init__(num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo)
    
    def atacarPlacaje(self):
        super().atacarPlacaje()

    def atacarAraniaso(self):
        super().atacarAraniaso()
    
    def atacarMordisco(self):
        super().atacarMordisco()
    
    def informacion(self):
        super().informacion()

    def atacarHidrobomba(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Hidrobomba")

    def atacarPistolaAgua(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Pistola de Agua")

    def  atacarBurbuja(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Burbuja")
    
    def atacarHidropulso(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Hidropulso")