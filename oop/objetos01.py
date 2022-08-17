class Gato:
    especie = "Felis silvestris catus" # atributo de clase

    def ponerNombre(self, n): # método (setter)
        x = 1 # variable local
        self.nombre = n # atributo de instancia

    def obtenerNombre(self): # getter
        #print(x) esto no funciona porque x es local de ponerNombre
        return self.nombre # esto funciona porque self.nombre NO ES una variable local, sino un atributo de cada objeto


gato1 = Gato() # instanciación -creación de un objeto-
michina = Gato() # otro gato

gato1.ponerNombre("Felix")
michina.ponerNombre("Michina")

print(f"El primer gato se llama {gato1.nombre} y es de la especie {gato1.especie}")

print(f"El segundo gato se llama {michina.nombre} y es de la especie {michina.especie}")

print(gato1.obtenerNombre())
