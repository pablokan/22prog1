# Ingresar la lluvia caída en milímetros para cada día de la semana. 
# Mostrar al final el total de lluvia caída y el nombre del día que más llovió.

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

def carga():
    mms = []
    for x in range(7):
        msg = "Ingrese la lluvia caída el " + dias[x] + ": "
        mm = int(input(msg))
        mms.append(mm)
    return mms

def totalLluvia(listaMMs):
    t = 0
    for i in range(len(listaMMs)):
        t += listaMMs[i]
    return t

def nombreDiaMasLluvioso(listaMMs):
    cM = 0
    for i in range(len(listaMMs)):
        if listaMMs[i] > cM:
            cM = listaMMs[i]
            nombre = dias[i]
    return nombre


milimetros = carga()
print("El total de lluvia caída en la semana fue", totalLluvia(milimetros))
print("El día que más llovió fue el", nombreDiaMasLluvioso(milimetros))




