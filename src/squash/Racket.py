import pygame
from pygame.locals import Rect

class Racket(Rect):
    def __init__(self, surface, color=(20, 100, 150),\
                       left=300, top=300, width=80, height=10):
        self.surface = surface
        self.COLOR = color
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def movex(self, delx):
        self.centerx += delx

    def movey(self, dely):
        self.centery += dely

    def draw(self):
        pygame.draw.rect(self.surface, self.COLOR, self)

