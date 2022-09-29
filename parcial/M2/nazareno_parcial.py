from dataclasses import dataclass
from os import system

# Parcial de Nazareno Bucciarelli - Comision: M2

@dataclass
class Cancion:
    nombre: str
    duracion: int

    def modificarDuracion(self):
        aux = self.duracion
        nuevaDuracion = input('Nueva duracion (seg): ')
        self.duracion = nuevaDuracion
        print(f'Duracion modificada de la cancion {self.nombre}. Antes duraba {aux}, ahora dura {nuevaDuracion} segundos.')

class Banda:

    def __init__(self,n, cc) -> None:
        self.nombre = n
        self.cantidadCanciones= cc
        self.listaCanciones = []

    def cargarTemas(self):
        system('clear')
        for i in range(self.cantidadCanciones):
            print(f'Cargando cancion N {i +1}')
            nombre=input(f'Nombre de la cancion: ')
            duracion=int(input(f'Duracion de la cancion (en seg): '))
            system('clear')
            self.listaCanciones.append(Cancion(nombre,duracion))
    
    def getListaCanciones(self):
        print(f'Lista de canciones de la banda {self.nombre}')
        for i in range(len(self.listaCanciones)):
            print(f'{i + 1}- Nombre: {self.listaCanciones[i].nombre} - Duracion: {self.listaCanciones[i].duracion}')
        input('Seleccione enter para continuar')
        system('clear')
        
    def modificarDuracion(self):
        nombresCanciones = []
        for cancion in self.listaCanciones:
            nombresCanciones.append(cancion.nombre)
        cancionSelect = input(f'Seleccione que cancion desea modificar su duracion: {nombresCanciones} ')
        for cancion in self.listaCanciones:
            if cancion.nombre.lower() == cancionSelect.lower():
                cancion.modificarDuracion()
        input('Seleccione enter para continuar')
        system('clear')

ledZeppelin = Banda('Led Zeppelin',3)
ledZeppelin.cargarTemas()
ledZeppelin.getListaCanciones()
ledZeppelin.modificarDuracion()
ledZeppelin.getListaCanciones()
