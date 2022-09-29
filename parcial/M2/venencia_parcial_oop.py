class Cancion:
    def __init__(self,nombreCan,duracion):
        self.Nombre = nombreCan
        self.Duracion = duracion
        
    def cambioDuracion(self):
        duracion = input("Inserte la nueva duracion: ")
        self.Duracion = duracion
        print(f"Cambio de duracion de la cancion:\n")
        self.Banda.mostrarCanciones()

class Banda:

    def __init__(self,nombre)-> None:
        self.NombreBanda = nombre

        self.listaCanciones = []
        
        listaCanciones2 = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]
        for i in range(len(listaCanciones2)):
            nombre = listaCanciones2 [i] [0]
            duracion = listaCanciones2 [i] [1]
            cancionActual = Cancion(nombre, duracion)
            self.listaCanciones.append(cancionActual)


    def mostrarCanciones(self):
        print(f"\nCanciones de la banda {self.NombreBanda}:\n")
        for cancion in self.listaCanciones:
            print(f"\n Cancion(nombre = {cancion.Nombre},duracion = {cancion.Duracion})\n")
    
banda1 = Banda("Led Zeppelin")
banda1.mostrarCanciones()






    


        
        

        
    