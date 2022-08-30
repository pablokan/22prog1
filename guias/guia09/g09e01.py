class Cuenta:
    def __init__(self, numero, dni, saldo, interes) -> None:
        self.numero = numero
        self.dni = dni
        self.saldo = saldo
        self.interes = interes

    def actualizarSaldo(self, cantidadDias):
        iD = self.interes / 365 * cantidadDias
        self.saldo = self.saldo + (self.saldo * iD / 100)

    def ingresar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= monto

    def __str__(self):
        return f"{self.numero} --- {self.saldo}"


cuenta = Cuenta(1, 123344, 100, 365)
print(cuenta)
cuenta.actualizarSaldo(10)
print(cuenta)
cuenta.ingresar(90)
print(cuenta)
cuenta.retirar(220)
print(cuenta)
cuenta.retirar(200)
print(cuenta)
