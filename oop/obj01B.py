class Persona:
    especie = "Homo Sapiens" # atributo de clase

    def setName(self, n): # setter (sirve para asignar valores a los atributos)
        self.name = n # atributo de instancia

primerHumano = Persona() # instanciación -creación del objeto-
primerHumano.setName("Adán")
print(primerHumano.name, primerHumano.especie)
primeraMujer = Persona()
primeraMujer.setName("Eva")
print(primeraMujer.name)
