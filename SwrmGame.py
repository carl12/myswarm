

class Game:
    def __init__(self,ai_In):
        self.mu = []
        for i in range(8):
            self.mu.append(MeatUnit(i))
        self.mu[0].amount = 35
        self.larva = 1
        self.ai_num = ai_In
        self.my_ai = ai(ai_In)
        self.time = 0

    def do_ai(self):
        self.my_ai.build(self)

    def ticN(self,time):
        for i in range(time):
            self.tic()

    def tic(self):
        self.meatUProd()
        self.larvaProd()
        self.terrProd()
        self.enrgProd()


    def meatUProd(self):
        for i in range(1,len(self.mu)):
            production = self.mu[i].production * self.mu[i].amount
            self.mu[i-1].add(production)

    def buy(self,tier,amount):
        cost = self.mu[tier].cost * amount
        if cost > self.mu[i-1].amount:
            self.mu[tier].buy(amount)
            self.mu[tier-1].use(cost)


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
        self.cost = tier
        self.prodUp = 0
        self.twinUp = 0
        self.myName = self.names[tier]
        self.amount = 0

    def getCost(self,tier):
        if tier < 10:
            return 10 ** tier
        else:
            raise 'tier math too high'

    @property
    def prod(self):
        print("it worked")
        return self.cost

    def buy(self,num):
        """Buy number before twins (will use up num larvae)"""
        self.amount += self.twinUp*num

    def add(self,num):
        self.amount += num

    def use(self,num):
        self.amount -= num




class ai:
    def __init__(self,type):
        self.type = type

    def build(self, game):
        return

