nombreBanda = "Led Zeppelin"
listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]


class Cancion():
    def __init__ (self,nombre,duracion):
        self.nombre=nombre
        self.duracion=duracion

    def __str__(self) -> str:
        return f"{self.nombre} - {self.duracion}"

class Banda ():
    def __init__ (self,nombreB):
        self.listaObjetoCanciones=[]
        self.nombreBanda=nombreB

        for cancion in listaCanciones:
            nombre= cancion[0]
            duracion= cancion[1]
            cancion = Cancion(nombre, duracion)
            self.listaObjetoCanciones.append(cancion)
            print (f"Canción: {cancion.nombre} - Duración: {cancion.duracion} segundos")  
 
    def cambioDuracion (self):
        print(listaCanciones)
        preg= "si"  
        preg= input ("Desea cambiar la duración de alguna canción? ")
        while preg == "si":
            cancion= input("Ingrese el nombre de la canción que desea modificar: ")
            for c in self.listaObjetoCanciones:
                if c.nombre.upper() == cancion.upper():
                    cd= int (input ("qué duración quiere ponerle? "))
                    c.duracion=cd
                    print (f"Cambio de duración de {c.nombre}: {c.duracion}")
            preg= input ("Desea cambiar otra cancion?: ")

    def getAll(self):
        for c in self.listaObjetoCanciones:
            print(c)

miBanda=Banda(nombreBanda)
miBanda.cambioDuracion()
miBanda.getAll()

            




