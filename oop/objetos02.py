class Perro:
    especie="Canis lupus familiaris" #atributo de clase
    def __init__(self, nombre, edad):
        # el constructor es un método especial
        # 1) se ejecuta automáticamente
        # 2) recibe los argumentos en la instaciación
        self.nombre = nombre
        self.edad = edad

    def ponerNombre(self, n): # método
        self.nombre = n # atributo de instancia

    def obtenerNombre(self):
        return self.nombre

    def obtenerDatos(self):
        return self.nombre, self.edad

p1 = Perro("Bobby", 3) # instanciación -creación del objeto-
print(p1.especie)
print(p1.nombre)
print(p1.obtenerNombre()) # lo mismo que usar el atributo pero accediendo con un getter
p2 = Perro("Sultán", 2)
nombre, edad = p2.obtenerDatos()
print(nombre, edad)