import pygame
from PIL import Image
import os.path
from Tribe import Tribe
from random import randrange
import Colors

COLORS = Colors.get_colors_list()
Tribes = []

path = "Res/Maps"
fileName = "alliance"
fileName += '.png'
In = 1

pygame.init()

image = Image.open(os.path.join(path,fileName))
size = image.size
SCREEN = pygame.display.set_mode(size)
title = pygame.display.set_caption("Pixel Tribes")
c = pygame.time.Clock()


running = True
im = image.convert("RGBA")
while running:
    event = pygame.event.get()
    for e in event:
        if e.type == pygame.QUIT:
            running = False



    img=pygame.image.load(os.path.join(path,fileName))
    if In == 1:
        for col in COLORS:
            Tribes.append(Tribe(col, randrange(50, 100), im))
    for tribe in Tribes:
        tribe.move(Tribes, im)
    mode = im.mode
    siz = im.size
    data = im.tobytes()
    surface = pygame.image.frombuffer(data, siz, mode)
    SCREEN.blit(surface, (0, 0))

    pygame.display.flip() # update the display
    c.tick(30) # only three images per second
    In += 1
pygame.quit()