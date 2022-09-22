nombres = ["Juan", "Pedro", "Ana"]
calles = ["9 de julio 1234", "Mendoza 345", "9 de julio 654"]

callesSinAltura = []
for x in range(len(calles)):
    pos = len(calles[x])
    car = ""
    while car != " ":
        pos -= 1
        car = calles[x][pos]
    calle = calles[x][:pos]
    callesSinAltura.append(calle)







