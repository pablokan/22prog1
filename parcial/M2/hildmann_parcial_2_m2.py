from dataclasses import dataclass



@dataclass
class banda:
    nombreBanda:str
    listaObjetos=[]
    def setCanciones(self,cantidad):
        
        
        for x in range (cantidad):
            nombreC=input("ingrese nombre de la cancion\n")
            duracionC=input("ingrese su duracion:\n")
            cancionObjeto=canciones(lista1.nombreBanda,nombreC,duracionC)
            self.listaObjetos.append(cancionObjeto)
        
        
        
    def getInfo(self):
        print (f"NOMBRE BANDA:\n{self.nombreBanda}")
        for x in range(len(self.listaObjetos)):
            
            print(f"cancion Nro{x+1}: {self.listaObjetos[x].nombre}, duracion: {self.listaObjetos[x].duracion}")

    def cambiarDuracion(self):
        posicion=int(input("ingrese el numero de la cancion que desea modificar la duracion:\nCancion Nro:"))
        duracionUsuario=int(input("ingrese nueva duracion:\n"))
        
        self.listaObjetos[posicion-1].duracion=duracionUsuario
        print(f"se cambio la duracion de: {self.listaObjetos[posicion-1].nombre} \n Su nueva duracion es: {duracionUsuario}")

@dataclass
class canciones(banda):
    nombre:str
    duracion:str


listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]

banda1=input("ingrese nombre de la banda:\n")
cantidadCanciones=int(input("ingrese la cantidad de canciones que desea ingresar:\n"))
lista1=banda(banda1)
lista1.setCanciones(cantidadCanciones)
lista1.getInfo()
lista1.cambiarDuracion()