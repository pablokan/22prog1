def foo(p1, p2, *args, n1="<eneuno>", n2="<enedos>", **kwargs):
    print(p1, p2)
    print(args)
    print(n1, n2)
    print(kwargs)


foo(1, 2, 3, 4, 5, n2="<nuevo n2>", n4="<enecuatro>", n1="<nuevo n1>", n3="<enetres>",  n5="q") # observen que los nominados que no existen van al diccionario pero pero pero no importa si están desordenados (siempre que estén todos despues de los posicionales y args)
