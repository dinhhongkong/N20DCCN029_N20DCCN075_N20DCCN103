import pygame, sys
from pygame.locals import *
from enum import Enum
pygame.init()
WINDOW_WIDTH = 723
WINDOW_HEIGHT = 800
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FONT = pygame.font.SysFont("cambria", 30, bold= True)
MENU_BG = pygame.image.load('img/menu.jpg')
ICON_O = pygame.transform.scale(pygame.image.load('img/O.png'),(110, 110))
ICON_X = pygame.transform.scale(pygame.image.load('img/X.png'),(110, 110))

class Screen(Enum):
    MENU = 1
    SELECT_ALGO = 2
    GAMING = 3

SCREEN = Screen.MENU



WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

