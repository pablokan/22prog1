class Persona:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def __str__(self) -> str:
        return f"Se llama {self.nombre}"

class Cliente(Persona):
    def __init__(self, nombre, tipoCuenta):
        super().__init__(nombre)
        self.tipoCuenta = tipoCuenta

unCliente = Cliente("Juan", "VIP")
print(unCliente)

