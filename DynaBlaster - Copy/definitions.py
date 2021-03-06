from enum import Enum
import  random
import pygame
from Coordinates import *

pygame.init()
worldx = 760
worldy = 520
iconSize = 40
img = 'playerup.png'
img2 = 'secondplayer.png'

"""monsterlx=random.randint(0,3)
monsterly=random.randint(9,12)

monsterl2x=random.randint(4,6)
monsterl2y=random.randint(4,8)

monsterl3x=random.randint(7,10)
monsterl3y=random.randint(0,3)"""


def make_matrix():
    Matrix = [[0 for x in range(20)] for y in range(20)]
    return  Matrix

wallsPositions = make_matrix()
wallsPositions[1][1] = -1
wallsPositions[1][2] = -1
wallsPositions[2][1] = -1
wallsPositions[round((worldx-40)/iconSize)][round((worldy-40)/iconSize)] = -1
wallsPositions[round((worldx-80)/iconSize)][round((worldy-40)/iconSize)] = -1
wallsPositions[round((worldx-40)/iconSize)][round((worldy-80)/iconSize)] = -1



def find_free_spot():
    free_spots = []
    for x in range(0,18):
        for y in range(0,12):
            if wallsPositions[x][y] == 0:
                coordinate = Coordinates(x, y)
                free_spots.append(coordinate)
    return free_spots



#zajednicka logika za prozore (Start i Close)
gameDisplay = pygame.display.set_mode((worldx, worldy))

pygame.display.set_caption('Dyna Blaster')

white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(worldx / 2), int(worldy / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)
