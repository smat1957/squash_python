import sys
import pygame
from pygame.locals import QUIT
import random

def fine():
    pygame.quit()
    sys.exit()

pygame.init()
WIDTH = 640
HEIGHT = 480
WSIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode( WSIZE )
pygame.display.set_caption( 'Squash(Bounding Ball)' )
clock = pygame.time.Clock()
FPS = 30

WHITE = (255,255,255)
RED = (255,0,0)
RADIUS = 10
x = random.randint( 0, WIDTH-1 )
y = 0
delx = dely = 5

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            fine()
            
    surface.fill( WHITE )
    pygame.draw.circle( surface, RED, (x,y), RADIUS )
    if y>=HEIGHT or y<0:
        dely = -dely
    if x>=WIDTH or x<0:
        delx = -delx
    x += delx
    y += dely
    pygame.display.update()
    clock.tick( FPS )
