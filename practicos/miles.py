from curses import KEY_PREVIOUS
from random import randint


def controlaCuatro(accion):
    m = ""
    while len(m) < 4:
        if accion == "genera":
            m = randint(1000, 9999)
        elif accion == "pide":
            m = input("Tiro? ")    
        m = list(dict.fromkeys(list(str(m))))
    return m

m = controlaCuatro("genera")
#print(f'Debugging ######## {m=} #########')
acierto = False
while not acierto:
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

