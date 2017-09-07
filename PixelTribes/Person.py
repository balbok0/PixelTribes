import random
from Colors import LAND, WATER

class Person:

    def __init__(self, color, power, wisdom, pos, sick = False):
        self.age = 0
        sickChance = random.random()
        if(sickChance > 0.995):
            self.sick = True
        if(sickChance > .75 and sick):
            self.sick = True
        else:
            self.sick  = False
        self.alive = True

        self.potency = 0
        self.color = color
        self.power = self.mutate(power)
        self.wisdom = self.mutate(wisdom)
        self.pos = pos


    def move(self, Tribes, im):
        if(self.power < self.age):
            self.alive = False
            return
        im.putpixel(self.pos, LAND)
        newpos = self.add_tuples(self.pos, self.step())
        newpos = (newpos[0], newpos[1])
        if(newpos[0] < im.size[0] and newpos[1] < im.size[1]):
            if(im.getpixel(newpos) == LAND):
                self.pos = newpos
            elif(im.getpixel(newpos) == self.color):
                for tribe in Tribes:
                    if(tribe.Color == self.color):
                        for someone in tribe.People:
                            if(newpos == someone.pos):
                                self.__add__(tribe, someone)
            elif(im.getpixel(newpos) != WATER): #Means that it's enemy
                for tribe in Tribes:
                    if(tribe.Color == im.getpixel(newpos)):
                        for someone in tribe.People:
                            if(someone.pos == newpos):
                                self.fight(someone)
                            break

                if(self.alive):
                    self.pos = newpos
                else:
                    return

            self.age += 1
            if(self.age > 18):
                self.potency += 1
            if(self.sick):
                self.power *= .9


        if(self.alive):
            im.putpixel(self.pos, self.color)

    def step(self):
        return(random.randint(-1, 1), random.randint(-1, 1))

    def add_tuples(self, x, y):
        z = []
        for i in range(0, len(x)):
            z.append(x[i] + y[i])
        return z

    def __add__(self, tribe, other):
        if(self.potency > 20 and other.potency > 20):
            self.potency = 0
            other.potency = 0
            tribe.People.append(Person(self.color, (self.power + other.power)/2,
                                       (self.wisdom + other.wisdom)/2, self.pos,
                                       self.sick and other.sick))

    def fight(self, other):
        if(other.alive):
            if(other.power >= self.power):
                self.alive = False
            else:
                self.power *= .95 if random.random() < self.age/100.0  else 1.05
                other.alive = False

    def mutate(self, var):
        mut_chance = random.random()
        if(mut_chance > .999):
            return var*(1 - random.random()%.25) if random.random() < .5 else var*(1 + random.random()%.25)
        elif(mut_chance > .99):
            return var*(1 - random.random()%.5) if random.random() < .5 else var*(1 + random.random()%.5)
        else:
            return var