# Ejemplo CON constructor
class Persona:
    especie = "Homo Sapiens" # atributo de clase

    def __init__(self, n, e): # constructor: se ejecuta automáticamente en el momento de la instanciación y recibe argumentos en la clase
        self.nombre = n
        self.edad = e

chaboncito = Persona("Adán", 0) # instanciación -creación de un objeto- envío los argumentos de inicialización al constructor en la clase
minita = Persona("Eva", 0)
print(chaboncito.especie, chaboncito.nombre)
print(minita.especie, minita.nombre, minita.edad)
