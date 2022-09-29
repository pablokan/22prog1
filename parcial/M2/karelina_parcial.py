nombreBanda= "Pink Floyd"
listaCanciones = [("Have a cigar", 452), ("High Hopes", 296), ("One of my turns", 512)]

class Cancion ():
    def __init__ (self,nombre,duracion):
        self.nombre=nombre
        self.duracion=duracion 

    

class Banda():
    def __init__(self,tituloBanda):
        self.tbanda=tituloBanda
        self.canciones=[]
       
        for cancion in listaCanciones:
            nombre=cancion[0]
            duracion= cancion[1]
            cancionesFav=Cancion(nombre,duracion)
            self.canciones.append(cancionesFav)
        
        for cancion in self.canciones:
            print (f" Canción: {cancion.nombre} - Duración: {cancion.duracion}")

    def cambioDuracion (self):
        print (self.canciones)
        preg="si"
        preg= input ("Desea cambiar la duración de alguna de las canciones que aparecen?: ")
        while preg== "si":
            c= input ("escriba el nombre de la canción que desea modificar: ")
            if c  in self.canciones:
                nuevaduracion= int (input("Ingrese la cantidad de segundos que quiere que dure la canción: "))
                c.duracion = nuevaduracion
                print (f"Cambio de duración de {c.nombre}: Canción: {c.nombre} - Duración: {c.duracion}")
            preg= input("desea cambiar otra canción?: ")



banda1=Banda(nombreBanda)
banda1.cambioDuracion()



