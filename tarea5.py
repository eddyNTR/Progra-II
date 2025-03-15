"""Descripción: Crea una clase Estudiante que tenga los siguientes atributos:
nombre (público)
edad (público)
_curso (protegido)
__calificacion (privado)
También debe tener los siguientes métodos:
mostrar_info(): Devuelve el nombre y la edad del estudiante.
asignar_calificacion(nueva_calificacion): Permite asignar una nueva calificación.
Restricciones: 🔹 El método asignar_calificacion solo debe permitir valores entre 0 y 100.
🔹 No se debe acceder directamente a __calificacion, sino a través de un método.
✅ Objetivo: Implementa la clase y prueba su funcionalidad."""

class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self._curso = curso
        self.__calificacion = None

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def asignar_calificacion(self, nueva_calificacion):
        if nueva_calificacion >= 0 and nueva_calificacion <= 100:
            self.__calificacion = nueva_calificacion
        else:
            return f"La calificación debe estar entre 0 y 100"

    def obtener_calificacion(self):
        return f"Nota: {self.__calificacion}"

estudiante = Estudiante("Juan", 20, "Matemáticas")
print(estudiante.mostrar_info())

estudiante.asignar_calificacion(85)
print(estudiante.obtener_calificacion())  

print("-------------------------------------------------------------------")

"""2 Problema: Simulación de un Banco
Descripción: Crea una clase CuentaBancaria con los siguientes atributos:
titular (público)
__saldo (privado)
Debe tener los siguientes métodos:
depositar(monto): Aumenta el saldo si el monto es positivo.
retirar(monto): Disminuye el saldo si el monto es menor o igual al saldo disponible.
mostrar_saldo(): Devuelve el saldo actual de la cuenta.
Objetivo: Crea una cuenta, deposita dinero, retira y verifica que no se pueda acceder directamente al saldo."""

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            return f"Deposito exitoso: saldo actual {self.__saldo}"
        else:
            return f"El monto debe ser positivo"
        
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            return f"Retiro exitoso: saldo actual {self.__saldo}"
        else:
            return f"Saldo insuficiente."
        
    def mostrar_saldo(self):
        return f"Saldo actual: {self.__saldo}"
    
cuenta = CuentaBancaria("Pedro Rojas")
print(cuenta.mostrar_saldo())
print(cuenta.depositar(500))
print(cuenta.mostrar_saldo())
print("-----------------")
print(cuenta.retirar(400))
print(cuenta.mostrar_saldo())
print("------------------")
print(cuenta.retirar(1000))
print(cuenta.mostrar_saldo())