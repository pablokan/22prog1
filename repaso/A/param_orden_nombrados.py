def foo(a, b, *args, n1="ene uno", **kwargs):
    print(a, b, args, n1, kwargs)

foo(1, 2, 3, 4, 5, xX="equisequis", n1="nuevo ene uno", nN="algo")