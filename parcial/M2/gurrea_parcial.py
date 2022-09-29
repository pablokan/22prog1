from dataclasses import dataclass

@dataclass
class Banda():
    nombre:str
    canciones:list
    cancionesDeLaBanda = [] 
    def mostrarCanciones(self):   
        
        for cancion in self.canciones:
            cancion = Canciones(cancion[0],cancion[1])
            respuesta = input('quiere modificar la cancion?:si/no ')
            if respuesta == 'si':
                duracionNueva = input('ingrese la duracion')
                cancion.cambiarDuracion(duracionNueva)
            self.cancionesDeLaBanda.append(cancion)
            print(cancion)            

@dataclass
class Canciones():
    nombre:str
    duracion:str

    def cambiarDuracion(self,duracionNueva):
        print(f'Se cambio la duracion de la cancion {self.nombre}')
        self.duracion = duracionNueva
        

    

listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]
ledZeppelin = Banda("Led Zepelling",listaCanciones)
ledZeppelin.mostrarCanciones()




