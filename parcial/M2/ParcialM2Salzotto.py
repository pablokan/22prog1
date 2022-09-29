from dataclasses import dataclass
 
@dataclass
class banda:
    nombreBanda:str
    listaObjetos=[]
    def nomCanciones(self,numCan):
        for x in range (numCan):
            nombre=input("Cancion: ")
            duracion=input("ingrese su duracion:\n")
            canObj=canciones(listCan.nombreBanda,nombre,duracion)
            self.listaObjetos.append(canObj)  
    def getData(self):
        print (f"nombre de la Banda:\n{self.nombreBanda}")
        for x in range(len(self.listaObjetos)):
            print(f"cancion {x+1}= {self.listaObjetos[x].nombre}, duracion= {self.listaObjetos[x].duracion}")
 
    def cambiarDuracion(self):
        posicion=int(input("cancion que quiere modificar: "))
        duracionUsuario=int(input("Nueva duracion: "))
        self.listaObjetos[posicion-1].duracion=duracionUsuario
        print(f"se cambio la duracion de {self.listaObjetos[posicion-1].nombre}; su nueva duracion es= {duracionUsuario}")
 
@dataclass
class canciones(banda):
    nombre:str
    duracion:str
 
banda1=input("ingrese nombre de la banda: ")
listCan=banda(banda1)
listCan.nomCanciones(2)
listCan.getData()
listCan.cambiarDuracion()
