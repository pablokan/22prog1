class Madre:
    v = 0

class A(Madre):
    def suma20(self):
        self.v = self.v + 20
        
class B(Madre):
    def suma30(self):
        self.v = self.v + 30

a1 = A()
a1.suma20()
b1 = B()
b1.suma30()
print(b1.v)

