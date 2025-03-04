from pokemones.pokemon import Pokemon

class Electrico(Pokemon):
    def __init__(self, num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo):
        super().__init__(num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo)

    def informacion(self):
        super().informacion()
    
    def atacarPlacaje(self):
        super().atacarPlacaje()
    
    def atacarAraniaso(self):
        super().atacarAraniaso()
    
    def atacarMordisco(self):
        super().atacarMordisco()

    def atacarImpactrueno(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Impactrueno")

    def punioTrueno(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Puño Trueno")
    
    def atacarRayo(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Rayo")
    
    def atacarRayoCarga(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Rayo Carga")
    
