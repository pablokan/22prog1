from dataclasses import dataclass

@dataclass
class Cancion:
    nombre: str
    duracion: int
    def setNombreCancion(self,nombreCancion):
        self.nombreCancion = nombreCancion
    def getNombreCancion(self):
        return self.nombreCancion
    def setDuracion(self,duracion):
        self.duracion = duracion
    def getDuracion(self):
        return self.duracion

class Banda:
    def __init__(self,nombreBanda):
        self.listaCanciones = []
        self.nombreBanda = nombreBanda
        preg = "SI"
        while preg.upper() == "SI":
            nombreCancion = input(f"Ingrese el nombre de la cancion: ")
            duracion = int(input(f"Ingrese la duracion de {nombreCancion} en segundos: "))
            cancion = Cancion(nombreCancion, duracion)
            self.listaCanciones.append(cancion)
            preg = input(f"Desea agregar otra cancion a la banda {nombreBanda}: ")
    def cambioDuracion(self):
        print("Cambio de duracion")
        for cancion in self.listaCanciones:
            print(f"{cancion.nombre} - {cancion.duracion}")
        preg = input(f"Desea cambiar la duracion de alguna cancion?: ")
        while preg.upper() == "SI":
            nC = input(f"Ingrese el nombre de la cancion que desea cambiar su duracion: ")
            for cancion in self.listaCanciones:
                if cancion.nombre.upper() == nC.upper():
                    print(f"Cancion: {cancion.nombre}. Duracion vieja: {cancion.duracion}")
                    dC = int(input(f"Ingrese la nueva duracion de {cancion.nombre}: "))
                    cancion.setDuracion(dC)
                    print(f"Cancion: {cancion.nombre}. Duracion nueva: {cancion.duracion}")
            preg = input(f"Desea cambiar la duracion de otra cancion? ")                
    def getInfoCanciones(self):
        print("------------------------------")
        print(f"{nombreBanda}")
        print(f"Cancion - Duracion (segundos)")
        for cancion in self.listaCanciones:
            print(f"{cancion.nombre} - {cancion.duracion}")

nombreBanda = input(f"Ingrese el nombre de la banda: ")
b1 = Banda(nombreBanda)   
b1.cambioDuracion()    
b1.getInfoCanciones()