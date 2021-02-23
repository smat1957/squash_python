import sys
import pygame
from pygame.locals import QUIT

def fine():
    pygame.quit()
    sys.exit()

pygame.init()
WIDTH = 640
HEIGHT = 480
WSIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode( WSIZE )
pygame.display.set_caption( 'Squash(Bound Ball)' )
clock = pygame.time.Clock()
FPS = 10

WHITE = (255,255,255)
RED = (255,0,0)
RADIUS = 10
x = surface.get_rect().centerx
y = 0
dely = 5

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            fine()
            
    surface.fill( WHITE )
    pygame.draw.circle( surface, RED, (x,y), RADIUS )
    if y>=HEIGHT or y<0:
        dely = -dely
    y += dely
    pygame.display.update()
    clock.tick( FPS )
