from dataclasses import dataclass 
@dataclass
class Cancion:
    nombre:str
    duracion:int
    def cambiarDuracion(self):
        nDuracion=input("Nueva duración:")
        self.duracion=nDuracion
        print(f"Se cambió la duración de {self.nombre}\nNueva Duración:{self.duracion}")

@dataclass
class Banda:
    nombre:str
    canciones:list
    listaCanciones=[]
    def __post_init__(self):
        for cancion in self.canciones:
            nombre=cancion[0]
            duracion=cancion[1]
            c=Cancion(nombre,duracion)
            self.listaCanciones.append(c)
    def cambiarDuracionB(self):
        listaNombres=[]
        for cancion in self.listaCanciones:
            listaNombres.append(cancion.nombre)
        nomCancion=""
        while nomCancion not in listaNombres:
            nomCancion=input(f"¿De que canción desea cambiar la duración?({listaNombres})")
            if nomCancion not in listaNombres:
                print(f"{nomCancion} no es el nombre de una canción, estos son: {listaNombres}")      
        for cancion in self.listaCanciones:
            if cancion.nombre == nomCancion:
                cancion.cambiarDuracion()
        
    def getCanciones(self):
        for cancion in self.listaCanciones:
            print(cancion)
ledZeppelin=Banda("Led Zeppelin",[("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)])
ledZeppelin.getCanciones()
ledZeppelin.cambiarDuracionB()
ledZeppelin.getCanciones()
