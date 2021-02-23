import sys
import pygame
from pygame.locals import QUIT,KEYDOWN,K_RIGHT,K_LEFT,Rect
import random

def fine():
    pygame.quit()
    sys.exit()

def key_event():
    for event in pygame.event.get():
        if event.type == QUIT:
            fine()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                racket.centerx += 15
            if event.key == K_LEFT:
                racket.centerx -= 15
    
pygame.init()
WIDTH = 640
HEIGHT = 480
WSIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode( WSIZE )
pygame.display.set_caption( 'Squash(Bounding Ball)' )
clock = pygame.time.Clock()
FPS = 20

WHITE = (255,255,255)
RED = (255,0,0)
RADIUS = 10
x = random.randint( 0, WIDTH-1 )
y = 0
delx = dely = 5
GREEN = (0,255,0)
SIZE = (WIDTH//2, HEIGHT-50, 80, 10)
racket = Rect( SIZE )

while True:
    key_event()            
    surface.fill( WHITE )
    pygame.draw.rect( surface, GREEN, racket )
    pygame.draw.circle( surface, RED, (x,y), RADIUS )
    if y>=HEIGHT or y<0:
        dely = -dely
    if x>=WIDTH or x<0:
        delx = -delx
    x += delx
    y += dely
    pygame.display.update()
    clock.tick( FPS )
