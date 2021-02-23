import sys
import pygame
from pygame.locals import QUIT,Rect,KEYDOWN,K_RIGHT,K_LEFT
import random

def fine():
    pygame.quit()
    sys.exit()

def key_event():
    for event in pygame.event.get():
        if event.type == QUIT:
            fine()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and racket.right < WIDTH:
                racket.centerx += 15
            if event.key == K_LEFT and racket.left > 0:
                racket.centerx -= 15

pygame.init()
WIDTH = 640
HEIGHT = 480
WSIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode( WSIZE )
pygame.display.set_caption( 'Squash' )
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
    pygame.draw.rect(surface, GREEN, racket)
    pygame.draw.circle( surface, RED, (x,y), RADIUS )
    ball_rect = Rect( (x-RADIUS, y-RADIUS, RADIUS*2, RADIUS*2) )
    if y<0 or racket.colliderect( ball_rect ):
        dely = -dely
    if x<0 or x>=WIDTH:
        delx = -delx
    if y>=HEIGHT:
        print( 'Game over' )
        break
    x += delx
    y += dely
    pygame.display.update()
    clock.tick( FPS )

fine()
