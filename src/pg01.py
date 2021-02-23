import sys
import pygame
from pygame.locals import QUIT

pygame.init()
WIDTH = 640
HEIGHT = 480
WSIZE = (WIDTH, HEIGHT)
surface = pygame.display.set_mode( WSIZE )
pygame.display.set_caption( 'Squash' )
clock = pygame.time.Clock()
FPS = 10
WHITE = (255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    surface.fill( WHITE )
    pygame.display.update()
    clock.tick( FPS )
