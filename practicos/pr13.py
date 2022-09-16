from random import randint

class Blackjack:
    def __init__(self) -> None:
        palos = ("Pique", "Corazón", "Diamante", "Trébol")
        valores = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
        self.mazo = [(x, y) for x in palos for y in valores]

    def vC(self, carta) -> int:
            if carta[1] in ["J", "Q", "K"]:
                s = 10
            elif carta[1] == "A":
                s = 11
            else:
                s = carta[1]
            return s
    
    def darPrimeraMano(self):
        pC = self.mazo.pop(randint(0, 51))
        vPC = self.vC(pC)
        sC = self.mazo.pop(randint(0, 51))
        vSC = self.vC(sC)
        suma = vPC + vSC
        if suma > 21:
            suma = 12
        print(pC, sC)
        return suma

    def pideCarta(self):
        oC = self.mazo.pop(randint(0, 51))
        print(oC)
        return self.vC(oC)


bj = Blackjack()
suma = bj.darPrimeraMano()
print(suma)
r = "s"
while r == "s":
    r = input("pide carta? ")
    v = 0
    if r == "s":
        v = bj.pideCarta()
    suma += v
    print(suma)

