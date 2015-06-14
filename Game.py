import MeatUnit

class Game:
    def __init__(self,ai_In):
        self.mu = []
        for i in range(8):
            self.mu.append(MeatUnit(i))
        self.mu[0].amount = 35
        self.larva = 1
        self.ai_num = ai_In
        self.my_ai = ai(ai_In)

    def do_ai(self):
        self.my_ai.build(self)

    def tic(self):
        self.meatProd()
        self.larvaProd()
        self.terrProd()
        self.enrgProd()


    def meatProd(self):
        return

    def larvaProd(self):
        return

    def terrProd(self):
        return

    def enrgProd(self):
        return



class MeatUnit:
    print("asdf")
    names = ['meat','drone','queen','hive']
    def __init__(self,tier):
        self.tier = tier
        self.cost = self.getCost(tier)
        self.prod = tier
        self.prodUp = 0
        self.twinUp = 0
        self.myName = self.names[tier]
        self.amount = 0


    def getCost(self,tier):
        if tier < 10:
            return 10 ** tier
        else:
            raise 'tier math too high'





class ai:
    def __init__(self,type):
        self.type = type

    def build(self, game):
        return

