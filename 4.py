from abc import ABC, abstractmethod

class Estudiante(ABC):
    @abstractmethod
    def obtener_promedio(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass

class EstudianteDeGrado(Estudiante):
    def __init__(self, nombre, notas):
        self.__nombre = nombre
        self.__notas = notas

    def obtener_promedio(self):
        return sum(self.__notas) / len(self.__notas)

    def mostrar_informacion(self):
        print(f"Estudiante de Grado: {self.__nombre}, Promedio: {self.obtener_promedio()}")

class EstudianteDePosgrado(Estudiante):
    def __init__(self, nombre, tesis_calificada):
        self.__nombre = nombre
        self.__tesis_calificada = tesis_calificada

    def obtener_promedio(self):
        return "Completa la tesis" if self.__tesis_calificada else "Tesis pendiente"

    def mostrar_informacion(self):
        print(f"Estudiante de Posgrado: {self.__nombre}, Tesis: {self.obtener_promedio()}")

# Demostración
estudiantes = [
    EstudianteDeGrado("Juan", [8.5, 9.0, 7.5]),
    EstudianteDePosgrado("Ana", True)
]

for estudiante in estudiantes:
    estudiante.mostrar_informacion()