from input_int import inputInt
from os import system

def menu(**ops):
    system('clear')
    print(ops)
    print('Menú', end='\n\n')
    d = {}
    cantItems = len(ops) + 1
    op = 0
    while op != cantItems:
        for i,v in enumerate(ops.items(), start=1):
            print(i, ')', v[0])
            d[i] = v[1]
        print(cantItems, ') Salir del Programa')
        op = inputInt('Opción: ', min=1, max=cantItems)
        if op != cantItems:
            eval(d[op]+'()', ops)

if __name__ == '__main__':
    def stop():
        input('Enter para volver al menú')

    def createUser():
        print('función createUser')
        stop()

    def delUser():
        print('función delUser')
        stop()

    def listUsers():
        print('función listUsers')
        stop()

    #menu(createUser='Crear usuario!', delUser='Borrar usuario', listUsers='Listar usuarios')

    def foo():
        print('foo')
        stop()
    def bar():
        print('bar')
        stop()
    menu(foo='foo', bar='bar')



