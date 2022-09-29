from dataclasses import dataclass


@dataclass
class Cancion:
    nombre: str
    duracion: int

    def setDuracion(self,duracion):
        self.duracion = duracion

@dataclass
class Banda():
    nombre: str
    listObjCanciones = []
    listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]
    
    for cancion in listaCanciones:
        cancionObj = Cancion(*cancion)
        listObjCanciones.append(cancionObj)

    def getNombre(self):
        print(f"Banda: {self.nombre}")
    
    def modificarDuracion(self):
        for cancion in self.listObjCanciones:
            print(f"Cancion: {cancion.nombre} - Duracion: {cancion.duracion}")
            modificarCancion = input("Modificar duracion? ")
            if modificarCancion == "si":
                nuevaDuracion = input("Duracion: ")
                cancion.setDuracion(nuevaDuracion)
                print(f"Cambio de duracion en {cancion.nombre}")
                print(f"Cancion: {cancion.nombre} - Duracion: {cancion.duracion}")
    

nuevaBanda = Banda("Led Zeppelin")
nuevaBanda.getNombre()
nuevaBanda.modificarDuracion()