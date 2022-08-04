from random import randint

def controlaCuatro(accion):
    zzz = ""
    while len(zzz) < 4:
        if accion == "genera":
            zzz = randint(1000, 9999)
        elif accion == "pide":
            zzz = input("Tiro? ")    
        zzz = list(dict.fromkeys(list(str(zzz))))
    return zzz

usuario = input("Jugador: ")
m = controlaCuatro("genera")
# print(f'######## {m=} #########')
acierto = False
intentos = 0
while not acierto:
    intentos += 1
    t = controlaCuatro("pide")
    regu = 0
    bien = 0
    for i in range(len(t)):
        if t[i] in m:
            if t[i] == m[i]:
                bien += 1
            else:
                regu += 1
    print(f"{bien} bien y {regu} regular")
    if bien == 4:
        acierto = True    

print(f"{''.join(m)}!!!!!!!")

a = open("repaso/A/ranking.txt", "a")
a.write(f"{usuario},{intentos}\n")
a.close()

