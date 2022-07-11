# Hay dos operaciones principales sobre strings
# 1) Buscar: find
# 2) Partir, Recortar: 
#   2.1) slicing: obtener sub cadena 
#   2.2) split: obtener una lista

t = "Ya llegamos al mes de julio"
posJulio = t.find("julio")
if posJulio == -1:
    print("Julio no está")
else:
    print("Julio está en la posición", posJulio)
    print("ahora lo puede poner en otra variable")
    mes = t[posJulio:] # recortamos desde la posición encontrada hasta el fondo
    print(mes)

tConvertidoEnLista = t.split() # sin argumento divide por espacio
print(tConvertidoEnLista)
separadoXmes = t.split(" mes ")
print(separadoXmes)
w = "juan---pedro---ana"
listaNombres = w.split("---")
print(listaNombres)
# uso mas común
stringSeparadaPorComas = "Juan,docente,43,activo"
listaDelDocente = stringSeparadaPorComas.split(",")
print(listaDelDocente)

print(t.upper())
n = "1231987166"
print(n.count("1"))

# otro ejemplo de slicing
fecha = "03/06/1965"
# una forma de separar la fecha (con slicing)
dia = fecha[:2]
mes = fecha[3:5]
anio = int(fecha[6:])
anio2 = fecha[-4:]
print("mes:", mes)
print(f"{anio=}")
print(f"{anio2=}")
edad = 2022 - anio # solamente funciona si convierto a entero
print(f"{edad=}")

# otra forma de separar la fecha (convirtiéndola en lista con split)
listaFecha = fecha.split("/")
print(f"{listaFecha=}")

for i in range(len(t)):
    print(t[i], end="+")

for i in range(len(fecha)):
    print(fecha[i], end="+")

