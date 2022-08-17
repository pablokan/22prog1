from dataclasses import dataclass

@dataclass(kw_only=True)
class Base:
  type: str
  counter: int = 0

@dataclass(kw_only=True)
class Foo(Base):
  id: int

a = Foo(type="tipo", id=1)
print(a)
b = Foo(type="algo", counter=11, id=2)
print(b)

def func(a,b,c=1, *args, d, e=None, f, **kwargs):
    print(a,b,c,args,d,e,f)

func("a", "b", "arg1", "arg2", d="d", f="f")

def func(a, b, /, c, d=40): # la barra significa que los anteriores son pos-only arguments
    print(f"a:{a}, b:{b}, c:{c}, d:{d}")

func("a", "b", "c", "d")
func("a", "b", c="c", d="d")

def func(a, b, *, c, d=40): # el asterisco significa que los posteriores son kw-only
    print(f"a:{a}, b:{b}, c:{c}, d:{d}")

func("a", "b", c="c", d="d")
