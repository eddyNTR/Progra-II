from pokemones.pokemon import Pokemon

class Planta(Pokemon):
    def __init__(self, num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo):
        super().__init__(num_pokedex, nombrePokemon, pesoPokemon, sexo, temporadaQueAparece, tipo)

    def informacion(self):
        super().informacion()
    
    def atacarAraniaso(self):
        super().atacarAraniaso()
    
    def atacarMordisco(self):
        super().atacarMordisco()
    
    def atacarPlacaje(self):
        super().atacarPlacaje()

    def atacarParalizar(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Paralizar")

    def atacarDrenaje(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Drenaje")

    def atacarHojaAfilada(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Hoja Afilada")

    def atacarLatigoCepa(self):
        print(f"Soy {self.nombrePokemon} y estoy atacando con Latigo Cepa")