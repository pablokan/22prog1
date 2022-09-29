from dataclasses import dataclass

@dataclass
class Banda:
    nombre: str
    canciones=[]
    def mostrarBanda(self):
        print(f"Canciones cargadas de {self.nombre}:")
        for temita in self.canciones:
            print(temita)

    def agregarCancion(self):
        name=input(f"Ingrese el nombre de la canción de {self.nombre}: ")
        duration=int(input(f"ingrese la duración en segundos de {name}: "))
        song=Cancion(name,duration)
        self.canciones.append(song)
        print(song,"\n")

    def cambiarDuracion(self):
        cambio=False
        elegirSong=input("¿A qué cancion le quieres cambiar la duración?: ")
        for tema in self.canciones:
            if elegirSong == tema.nombre:
                tema.cambiarDuracion(elegirSong)
                print(tema,"\n")
                cambio=True
        if not cambio:
            print(f"La canción '{elegirSong}' no está agregada o la escribiste mal.")
    
@dataclass
class Cancion:
    nombre:str
    duracion:int
        
    def cambiarDuracion(self,temaCambiado):
        nuevaDuracion=int(input(f"Ingrese la nueva duración: "))
        self.duracion=nuevaDuracion
        print(f"\nLa duración de {temaCambiado} ha actualizado correctamente:")

bandita=Banda("Led Zeppelin")
bandita.agregarCancion()
bandita.agregarCancion()
bandita.cambiarDuracion()
bandita.agregarCancion()


#bandita.mostrarBanda()
