import sys
import pygame
from pygame.locals import QUIT
import random

pygame.init()
WIDTH = 640
HEIGHT = 480
WSIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode( WSIZE )
pygame.display.set_caption( 'Squash' )
clock = pygame.time.Clock()
FPS = 2

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
COLORS = [RED, GREEN, BLUE,\
          YELLOW, CYAN, MAGENTA, WHITE, BLACK]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    n = random.randint( 0, 7 )
    surface.fill( COLORS[n] )
    pygame.display.update()
    clock.tick( FPS )
