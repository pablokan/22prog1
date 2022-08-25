class A:
    def a(self):
        print("a")

    def mismo(self):
        print("mismo A")

class B:
    def b(self):
        print("b")

    def mismo(self):
        print("mismo B")

class C(A, B):
    pass


c = C()
c.a()
c.b()
c.mismo()
