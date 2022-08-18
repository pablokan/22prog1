class Puma: # Esta clase no tiene constructor
    def setEdad(self, e):
        self.edad = e

    def __str__(self): #dunder double underscore
        return f"Soy el pumita"

pumita = Puma() # al no tener constructor, no puedo pasar argumentos a la clase
pumita.setEdad(1)
print(f"El pumita tiene {pumita.edad} año")
print(pumita)
print(dir(pumita))

print(dir("hola")) # la función dir devuelve todos los métodos y atributos de un objeto