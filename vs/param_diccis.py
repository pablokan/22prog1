def foo(p1, p2, *args, n1="uno", n2 = "dos", **kwargs):
    print(p1, p2, args, n1, n2, kwargs)


foo(1, 2, n3="enetres", n4="enecuatro", n2="nuevo n2")
