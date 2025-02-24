from platos.plato import Plato
from platos.pique import Pique
from platos.charque import Charque
from platos.chicharron import Chicharon

pique = Pique("Pique macho", 80, "grande")
charque = Charque("Charquekan", 50, "con extra queso")
chicharon = Chicharon("Chicharron", 60, "si")

pique.mostrar_info()
pique.entregar_plato()
pique.recojer_plato()
print(" ")
charque.mostrar_info()
charque.entregar_plato()
charque.recojer_plato()
print("")
chicharon.mostrar_info()
chicharon.entregar_plato()
chicharon.recojer_plato()