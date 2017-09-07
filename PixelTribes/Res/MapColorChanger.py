import pygame
from PIL import Image
import os.path
import glob

#Colors
LAND    = (   0, 255,  33, 255)
WATER   = (   0,  38, 255, 255)
BLUE    = (   0,   0, 255, 255)
PINK    = (   0,   0, 234, 255)
BLACK   = (   0,   0,   0, 255)
WHITE  =  ( 255, 255, 255, 255)


path = "Res/Maps"
fileName = "alliance"
fileName += '.png'
In=1
pygame.init()

image = Image.open(os.path.join(path,fileName))
#SCREEN = pygame.display.set_mode(size)
#title = pygame.display.set_caption("Pixel Tribes")
c = pygame.time.Clock()
running = True
for fPath in glob.glob("./Res/Maps/*.png"):
    print(os.path.basename(fPath))
    im = Image.open(fPath)
    im = im.convert("RGBA")
    size = im.size
    print(im.size)
    ColorTuples = im.getcolors()
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            pixel = im.getpixel((x,y))
            try:
                if pixel[2] > 150 and pixel != WHITE:
                    im.putpixel((x, y), WHITE)
                elif pixel[1] > 150 and pixel != WHITE:
                    im.putpixel((x, y), BLACK)
            except IndexError:
                print((x, y))
                break


    im.save(os.path.basename(fPath))

