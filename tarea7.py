#Ejercicio 7: Sistema de Gestión de Empleados Crea una clase Empleado con los siguientes requisitos: 1️⃣ Método de instancia mostrar_info(self): Debe imprimir el nombre, puesto y salario del empleado. 2️⃣ Método de clase contar_empleados(cls): Debe contar cuántos empleados han sido creados. 3️⃣ Método estático es_salario_valido(salario): Debe verificar si el salario es mayor o igual a 1000: ✅ Paso 1: Crea la clase Empleado con los atributos (nombre, puesto, salario) y métodos requeridos. ✅ Paso 2: Agrega un contador de empleados en la clase. ✅ Paso 3: Verifica si el salario ingresado es válido antes de crear un empleado si no es valido (salario <= 1000). agrega 1000 como salario por defecto. ✅ Paso 4: Crea varios empleados y usa los métodos para mostrar información y contar empleados. una vez terminado...🔹 Agrega un método aumentar_salario(self, porcentaje).🔹 Agrega un método promocionar(self, nuevo_puesto).
"""class Empleado:
    contador_empleados = 0  # Atributo de clase para contar empleados

    def __init__(self, nombre, puesto, salario):
        self.__nombre = nombre
        self.__puesto = puesto
        self.__salario = Empleado.es_salario_valido(salario)
        Empleado.contador_empleados += 1  # Aumentar el contador de empleados

    def __str__(self):  # Método de instancia
        return f"Empleado: {self.__nombre}, Puesto: {self.__puesto}, Salario: {self.__salario}"
    
    def mostrar_info(self):
        return f"Empleado: {self.__nombre}, Puesto: {self.__puesto}, Salario: {self.__salario}"

    @classmethod
    def contar_empleados(cls):
        return f"Se han registrado {cls.contador_empleados} empleados."
    
    @staticmethod
    def es_salario_valido(salario):
        if salario >= 1000:
            return salario
        else:
            return 1000

    def aumentar_salario(self, porcentaje):
        return f"{self.__nombre} su salario con el aumento sera {self.__salario + (self.__salario * porcentaje)}"

    def promocionar(self, nuevo_puesto):
        self.__puesto = nuevo_puesto
        return f"El empleado {self.__nombre} cambio de puesto a {self.__puesto}"

# Crear empleados
emp1 = Empleado("Ana", "Desarrolladora", 2000)
emp2 = Empleado("Carlos", "Analista", 1500)

# Mostrar información de empleados
print(emp1.mostrar_info())
print(emp2.mostrar_info())

print(emp1.aumentar_salario(0.20))
print(emp2.promocionar("Gerente"))

# Contar empleados
print(Empleado.contar_empleados())

emp3 = Empleado("Luis", "Trainee", 800)  # Esto debe mostrar de salario 1000
print(emp3.mostrar_info())
"""

#Ejercicio 8: Gestión de Vehículos Objetivo: Crear una clase Vehiculo que permita gestionar diferentes vehículos, llevando un control de cuántos se han creado y validando si su velocidad es segura (si es mayor a 100 km/h entonces mantener la velocidad en 100Km/h).🔹 Requisitos: 1️⃣ Método de instancia descripcion(self): Debe devolver una cadena con la marca, modelo y velocidad máxima del vehículo. 2️⃣ Método de clase total_vehiculos(cls): Debe devolver la cantidad total de vehículos creados. 3️⃣ Método estático es_velocidad_segura(velocidad): Debe verificar si la velocidad es menor o igual a 100 km/h.

"""class Vehiculo:
    contador_vehiculos = 0  # Atributo de clase para contar vehículos

    def __init__(self, marca, modelo, velocidad_maxima):
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad_maxima = Vehiculo.es_velocidad_segura(velocidad_maxima)
        Vehiculo.contador_vehiculos += 1  # Aumentar el contador de vehículos

    def descripcion(self):
        return f"Vehículo: Marca: {self.__marca}, Modelo: {self.__modelo}, Velocidad Máxima: {self.__velocidad_maxima} km/h"

    @classmethod
    def total_vehiculos(cls):
        return f"Se han registrado {cls.contador_vehiculos} vehículos."

    @staticmethod
    def es_velocidad_segura(velocidad):
        if velocidad > 100:
            return 100
        else:
            return velocidad

veh1 = Vehiculo("Toyota", "Corolla", 150)
veh2 = Vehiculo("Honda", "Civic", 50)

print(veh1.descripcion())
print(veh2.descripcion())

print(Vehiculo.total_vehiculos())

veh3 = Vehiculo("Ford", "Focus", 110) 
print(veh3.descripcion())"""

#Sistema de Gestión de Estudiantes📌 Objetivo: Crear una clase Estudiante que permita gestionar un grupo de estudiantes, calcular promedios y verificar si aprobaron o reprobaron.🔹 Requisitos: 1️⃣ Método de instancia mostrar_info(self): Muestra el nombre, edad y promedio del estudiante.2️⃣ Método de clase total_estudiantes(cls): Devuelve la cantidad total de estudiantes registrados.3️⃣ Método estático es_aprobado(promedio): Retorna True si el promedio es mayor o igual a 60, False si es menor.4️⃣ Método de instancia actualizar_notas(self, nueva_lista_notas): Permite actualizar las notas de un estudiante y recalcular su promedio.5️⃣ Método de clase mejor_estudiante(cls, lista_estudiantes): Recibe una lista de estudiantes y devuelve al que tiene el mejor promedio.

class Estudiante:
    contador_estudiantes = 0 

    def __init__(self, nombre, edad, lista_notas):
        self.__nombre = nombre
        self.__edad = edad
        self.__lista_notas = lista_notas
        self.__promedio = self.calcular_promedio()
        Estudiante.contador_estudiantes += 1 

    def calcular_promedio(self):
        if self.__lista_notas:
            return sum(self.__lista_notas) / len(self.__lista_notas)
        else:
            return 0

    def mostrar_info(self):
        return f"Estudiante: {self.__nombre}, Edad: {self.__edad}, Promedio: {self.__promedio}"

    @classmethod
    def total_estudiantes(cls):
        return f"Se han registrado {cls.contador_estudiantes} estudiantes."

    @staticmethod
    def es_aprobado(promedio):
        return promedio >= 60

    def actualizar_notas(self, nueva_lista_notas):
        self.__lista_notas = nueva_lista_notas
        self.__promedio = self.calcular_promedio()

    @classmethod
    def mejor_estudiante(cls, lista_estudiantes):
        if not lista_estudiantes:
            return None
        mejor = lista_estudiantes[0]
        for estudiante in lista_estudiantes:
            if estudiante.__promedio > mejor.__promedio:
                mejor = estudiante
        return mejor

est1 = Estudiante("Juan", 20, [60, 56, 92])
est2 = Estudiante("Maria", 22, [85, 99, 100])
est3 = Estudiante("Pedro", 21, [50, 60, 25])

print(est1.mostrar_info())
print(est2.mostrar_info())
print(est3.mostrar_info())


print(f"{est1.mostrar_info()} - Aprobado: {Estudiante.es_aprobado(est1.calcular_promedio())}")
print(f"{est2.mostrar_info()} - Aprobado: {Estudiante.es_aprobado(est2.calcular_promedio())}")
print(f"{est3.mostrar_info()} - Aprobado: {Estudiante.es_aprobado(est3.calcular_promedio())}")

print(Estudiante.total_estudiantes())

est3.actualizar_notas([70, 75, 80])
print(est3.mostrar_info())

mejor_est = Estudiante.mejor_estudiante([est1, est2, est3])
print(f"El mejor estudiante es: {mejor_est.mostrar_info()}")