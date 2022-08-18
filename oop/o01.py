class Persona:
    especie = "Homo Sapiens" # atributo de clase, vale para todos los objetos creados de tipo Persona

    # El constructor se ejecuta cuando se crea el objeto y recibe los argumentos en los paréntesis de la clase
    def __init__(self, n, e=99): # constructor
        self.nombre = n # atributo de instancia, vale distinto para cada objeto Persona
        self.edad = e

    def setName(self, n):
        self.nombre = n

    def getName(self): # getter
        return self.nombre

    def __str__(self):
        return f"Persona, género {self.especie}, llamada {self.nombre}, de {self.edad} años de edad"

# instanciación = creación del objeto
chaboncito = Persona("Adán") # instanciación
chaboncito.setName("Hermenegildo")
print(chaboncito.nombre)
minita = Persona("Eva")
print(minita.nombre) # viola el encapsulamiento
print(minita.getName()) # respeta el encapsulamiento

print(minita)

