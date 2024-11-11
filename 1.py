from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

    @abstractmethod
    def conducir(self):
        pass

class Coche(Vehiculo):
    def encender(self):
        print("El coche está encendido.")

    def apagar(self):
        print("El coche está apagado.")

    def conducir(self):
        print("El coche está en marcha.")

class Bicicleta(Vehiculo):
    def encender(self):
        print("La bicicleta no necesita encenderse.")

    def apagar(self):
        print("La bicicleta no necesita apagarse.")

    def conducir(self):
        print("Estás pedaleando la bicicleta.")

# Demostración
coche = Coche()
bicicleta = Bicicleta()

coche.encender()
coche.conducir()
coche.apagar()

bicicleta.encender()
bicicleta.conducir()
bicicleta.apagar()