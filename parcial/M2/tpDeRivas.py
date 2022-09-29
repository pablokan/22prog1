from dataclasses import dataclass,field

@dataclass
class Banda:
    nombre: str
    canciones: list

    def __post_init__(self) -> None: #Transformo mi lista de canciones en una lista de objetos Cancion
        cancionesObjeto = []
        for cancion in listaCanciones:
            nombre = cancion[0]
            duracion = cancion[1]
            c1 = Cancion(nombre, duracion)
            cancionesObjeto.append(c1)
        self.canciones = cancionesObjeto

    def cambiarDuracion(self, numero, duracion): #Debo elegir que numero de cancion quiero cambiar la duracion y darle su nueva duracion
        self.canciones[numero].setDuracion(duracion)

    def __repr__(self) -> str: #String que nos dara cada banda y cada cancion
        cancionesOrdenadas = sorted(self.canciones)
        stringCanciones = "\n"
        for cancion in cancionesOrdenadas: #Crea el string de los datos de cada cancion
            stringCanciones += cancion.__repr__() +"\n"
        return f"Nombre de la banda: {self.nombre} {stringCanciones}"

@dataclass (order=True)            
class Cancion:
    orden: any = field(init=False, repr=False)
    nombre:str
    duracion: int

    def __post_init__(self):
        self.orden = self.duracion

    def setDuracion(self, nuevaDuracion):
        print(f"Cambio de duracion de {self.nombre} \n")
        self.duracion = nuevaDuracion
        self.orden = self.duracion

    def __repr__(self) -> str: #String de como se vera cada cancion
        return f"Nombre: {self.nombre} Duracion: {self.duracion}"

nombreBanda = "Led Zeppelin"
listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]

b1 = Banda(nombreBanda, listaCanciones)
print(b1)

b1.cambiarDuracion(2, 220)
print(b1)