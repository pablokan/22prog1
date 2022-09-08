class Animal:
    def __init__(self) -> None:
        self.reino = "Reino Animal"

    def getReino(self):
        return self.reino

class Mammal(Animal):
    def __init__(self) -> None:
        super().__init__()

class Cat(Mammal):
    def __init__(self) -> None:
        super().__init__()

kitty = Cat()
print(kitty.getReino())