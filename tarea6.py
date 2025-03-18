#Gestión de Empleados Objetivo: Crear una clase Empleado que gestione la información de los empleados de una empresa utilizando encapsulamiento. Se deberán implementar métodos getter, setter y deleter para los atributos privados, respetando algunas restricciones. Requisitos de la Clase Empleado: Atributos (todos privados): __nombre (tipo str): Nombre del empleado. Restricción: Una vez establecido, no se debe permitir modificarlo. __edad (tipo int): Edad del empleado. Restricción: La edad debe ser mayor o igual a 18. __salario (tipo float): Salario del empleado. Restricción: El salario no puede ser negativo (debe ser mayor o igual a 0). Métodos metodos getter, setter y deleter que veas nesesario. __ init __ __ del __ __ str __. Tambien se de calcular los aportes del asegurado que es del; 12.71% sobre el salario. Calcular el liquido pagable al trabajador. ccalcular los aportes patronales de la empresa (aporte laboral) a la gestora que es del 16.71% sobre el salario

class Empleado():
    def __init__(self, nombre, edad, salario):
        self.__nombre = nombre
        self.__edad = edad
        self.__salario = salario

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        if edad >= 18:
            self.__edad = edad
        else:
            raise ValueError("La edad debe ser mayor o igual a 18 años")
        
    @edad.deleter
    def edad(self, edad):
        print("eliminando edad...")
        del self.__edad

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        if salario >= 0:
            self.__salario = salario
        else:
            raise ValueError("El salario debe ser mayor o igual a cero")
        
    @salario.deleter
    def salario(self, salario):
        print("Eliminando salario......")
        del self.__salario

    def aporter_asegurado(self):
        return self.__salario * 0.1271
    
    def liquido_pagable(self):
        return self.__salario - self.aporter_asegurado()
    
    def aporte_patronal(self):
        return self.__salario * 0.1671
    
    def __str__(self):
        return f"Empledo: {self.__nombre}, Edad: {self.__edad}, Salario: {self.__salario} Bs."
    
    def __del__(self):
        print(f"Empleado {self.__nombre} ha sido eliminado")
        
    
empleado = Empleado("Pedro Sanchez", 23, 5000)
print(empleado)
print(f"Aportes del asegurado {empleado.nombre}, son {empleado.aporter_asegurado()} Bs.")
print(f"Liquido pagable del empleado {empleado.nombre}, es {empleado.liquido_pagable()} Bs.")
print(f"Aportes patronales de {empleado.nombre} son, {empleado.aporte_patronal()} Bs.")
print("--------------")
del empleado