from random import randint
n = ""
while len(n) < 4:
    n = randint(1000, 9999)
    n = str(n)
    print(n)
    #n = list(dict.fromkeys(list(str(n))))
    numeroEnFormatoLista = list(n) 
    print(numeroEnFormatoLista)
    d = dict.fromkeys(numeroEnFormatoLista, "pipa")
    print(d)
    n = list(d)
    print(n)



