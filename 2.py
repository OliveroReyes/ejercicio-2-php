class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Saldo actual: {self.__saldo}")
        else:
            print("Cantidad inválida para depositar.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Saldo actual: {self.__saldo}")
        else:
            print("Cantidad inválida para retirar.")

    def get_saldo(self):
        return self.__saldo

# Demostración
cuenta = CuentaBancaria("12345678", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
print("Saldo final:", cuenta.get_saldo())