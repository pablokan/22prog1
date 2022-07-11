import os

def cargaClientes():
    print("Este es carga de clientes")
    input("Oprima Enter para volver al menú")

def listadoClientes():
    print("Este es listado de clientes")
    input("Oprima Enter para volver al menú")

op = ""
while op != "3":
    os.system ("clear") # "cls" en Windows
    print("Menú de Opciones")
    print("1) Carga de Clientes")
    print("2) Listado de Clientes")
    print("3) Salir")
    op = input("Ingrese una opción: ")
    if op == "1":
        cargaClientes()
    elif op == "2":
        listadoClientes()
