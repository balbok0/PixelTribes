from Person import Person
import random
from random import randrange
import Colors

class Tribe:

    def __init__(self, Color, population, image):
        self.Color = Color
        self.People = []
        pos = (0, 0)
        done = False
        im = image.convert("RGBA")
        while not done:
            pos = (random.randint(0, image.size[0]-1), random.randint(0, image.size[1]-1))
            if(im.getpixel(pos) == Colors.LAND):
                done = True
        for i in range(0, population):
            done = False
            while not done:
                its_pos = (pos[0] + random.randint(0, 50) if random.random() > .5 else pos[0] - random.randint(0, 50),
                           pos[1] + random.randint(0, 50) if random.random() > .5 else pos[1] - random.randint(0, 50))
                if (im.getpixel(its_pos) == Colors.LAND):
                    done = True

            self.People.append(Person(Color, randrange(200, 500), randrange(0, 50), its_pos))

    def move(self, Tribes, img):
        for person in self.People:
            if(person.alive):
                person.move(Tribes, img)
            else:
                img.putpixel(person.pos, Colors.LAND)
                self.People.remove(person)