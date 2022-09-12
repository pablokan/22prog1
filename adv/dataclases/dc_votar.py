from dataclasses import dataclass, astuple, asdict, field


@dataclass
class Person:
    name: str
    age: int
    iq: int = field(init=False, repr=False)
    mayor: bool = False

    def __post_init__(self):
        self.mayor = True if self.age  >= 18 else False 

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age


p = Person('Jane Doe', 25)
print(p.getName())
p.setAge(20)


q = Person('John Doe', 17)
print(q)
# print(astuple(q))
# print(asdict(q))

