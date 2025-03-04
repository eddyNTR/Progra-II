from pokemones.pokemon import Pokemon

class Fuego(Pokemon):
    def __init__(self, num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo, ):
        super().__init__(num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo)

    def informacion(self):
        super().informacion()
        
    def atacarPlacaje(self):
        super().atacarPlacaje()

    def atacarAraniaso(self):
        super().atacarAraniaso()

    def atacarMordisco(self):
        super().atacarMordisco()

    def atacarPunioFuego(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Puño Fuego")
    
    def atacarAscuas(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Ascuas")
    
    def atacarLanzallamas(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con")