from pokemones.pokemon import Pokemon
from pokemones.electrico import Electrico
from pokemones.fuego import Fuego
from pokemones.planta import Planta
from pokemones.agua import Agua

charmander = Fuego(4, "Charmander", 8.5, "Macho", "Primavera", "Fuego")
bulbasaur = Planta(1, "Bulbasaur", 6.9, "Hembra", "Otoño", "Planta")
pikachu = Electrico(25, "Pikachu", 6.0, "Macho", "Verano", "Electrico")
squirtle = Agua(7, "Squirtle", 9.0, "Hembra", "Invierno", "Agua")

charmander.informacion()
print("-------------------------")
charmander.atacarPlacaje()
charmander.atacarAraniaso()
charmander.atacarMordisco()
charmander.atacarPunioFuego()
charmander.atacarAscuas()
charmander.atacarLanzallamas()
print("-------------------------")
print(" ")
bulbasaur.informacion()
print("-------------------------")
bulbasaur.atacarPlacaje()
bulbasaur.atacarAraniaso()
bulbasaur.atacarMordisco()
bulbasaur.atacarParalizar()
bulbasaur.atacarDrenaje()
bulbasaur.atacarHojaAfilada()
bulbasaur.atacarLatigoCepa()
print("-------------------------")
print(" ")
pikachu.informacion()
print("-------------------------")
pikachu.atacarPlacaje()
pikachu.atacarAraniaso()
pikachu.atacarMordisco()
pikachu.atacarImpactrueno()
pikachu.punioTrueno()
pikachu.atacarRayo()
pikachu.atacarRayoCarga()
print("-------------------------")
print(" ")
squirtle.informacion()
print("-------------------------")
squirtle.atacarPlacaje()
squirtle.atacarAraniaso()
squirtle.atacarMordisco()
squirtle.atacarHidrobomba()
squirtle.atacarPistolaAgua()
squirtle.atacarBurbuja()
squirtle.atacarHidropulso()
print("-------------------------")