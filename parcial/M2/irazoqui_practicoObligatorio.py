class Banda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.listaDeCanciones = []      

    def nuevaCancion(self,nombre,duracion):
        nuevaCancion = Cancion(nombre,duracion)
        self.listaDeCanciones.append(nuevaCancion)

    def setDuracion(self,nombreABuscar,nuevaDuracion):
        for e in self.listaDeCanciones:
            if e.getNombre() == nombreABuscar:
                e.setDuracion(nuevaDuracion) 

    def salida(self):
        print(f'''Nombre de la banda: {self.nombre}
Lista de canciones:''')
        for e in self.listaDeCanciones:
            print(e)

class Cancion:
    def __init__(self,nombre,duracion):
        self.nombre = nombre
        self.duracion = duracion

    def setDuracion(self,nuevaDuracion):
        print(f'Cambio de duración en la canción {self.nombre}:')
        self.duracion = nuevaDuracion
        print(self)

    def getNombre(self):
        return self.nombre

    def __str__(self) -> str:
        return f'-Canción: {self.nombre}. Duración: {self.duracion} minutos.'


if __name__ == '__main__':
    nombreBanda = 'Led Zeppelin'
    listaCanciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]

    nuevaBanda = Banda(nombreBanda)
    for e in listaCanciones:
        nuevaBanda.nuevaCancion(e[0],e[1])

    nuevaBanda.salida()
    nuevaBanda.setDuracion('Black dog',321)

