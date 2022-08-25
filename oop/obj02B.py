class Persona:
    especie = "Homo Sapiens" # atributo de clase

    def __init__(self, n): # constructor (sirve para inicializar atributos)
        # 1) se ejecuta automáticamente en la instanciación
        # 2) recibe sus argumentos en la clase
        self.name = n # atributo de instancia

    def getName(self):
        return self.name

primerHumano = Persona("Adán")
print(primerHumano.name, primerHumano.especie)
primeraMujer = Persona("Eva")
print(primeraMujer.name) # violación del encapsulamiento
print(primeraMujer.getName()) # encapsulamiento

