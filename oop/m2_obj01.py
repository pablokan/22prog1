# Ejemplo base sin constructor
class Persona:
    especie = "Homo Sapiens" # atributo de clase

    def setName(self, n): # setter: un método que sirve para asignar valores a los atributos
        self.nombre = n # atributo de objeto

chaboncito = Persona() # instanciación -creación de un objeto-
minita = Persona()
chaboncito.setName("Adán")
minita.setName("Eva")
print(chaboncito.especie, chaboncito.nombre)
print(minita.especie, minita.nombre)
