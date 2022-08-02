from input_int import inputInt

def inputMenu(listaOpc, mensaje='Elija una opción'):
    mensaje = mensaje + ": "
    listaOpc = listaOpc.split('/')
    for indice in range(len(listaOpc)):
        print(f"{indice+1}) {listaOpc[indice]}")
    op = inputInt("Ingrese opción: ", 1, len(listaOpc))
    return listaOpc[op-1]

if __name__=='__main__':
    q = inputMenu('si/no/a veces')
    print(q)
    r = inputMenu('rojo/verde', 'Elija un color')
    print(r)
