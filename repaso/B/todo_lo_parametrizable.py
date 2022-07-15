def foo(pos1, pos2, *args, n1="ene uno", **kwargs):
    print(pos1, pos2, args, n1, kwargs)

foo(1, 2, 3, 4, 5, "pepito", a="este es a", n1="nuevo ene uno", b="este es b")

