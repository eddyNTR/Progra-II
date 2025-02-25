from personas.profesor import Profesor
from personas.estudiante import Estudiante
from personas.director import Director
from personas.persona import Persona

profesor = Profesor("Juan", 30, "Profesor", "Masculino", "Av. petrolera", "Licenciado", "Programacion", 5000, "Mañama")
estudiante = Estudiante("Pedro", 20, "Estudiante", "Masculino", "Av petrolera", "3ro", "2019-123", 100)
director = Director("Maria", 40, "Director", "Femenino", "Av. America", "Casada", "Mañana")

profesor.presentacion()
profesor.saludar()
profesor.evaluar()
profesor.asistencia()
profesor.tomar_lista()
profesor.educar()
print(" ")
estudiante.presentacion()
estudiante.saludar()
estudiante.asistencia()
estudiante.estudiar()
estudiante.hacer_tarea()
estudiante.aprobar()
print(" ")
director.presentacion()
director.saludar()
director.asistencia()
director.tomar_decisiones()
director.administrar()
director.decomisar()
