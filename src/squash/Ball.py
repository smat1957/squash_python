from math import sin, cos, radians
from random import randint
import pygame
from pygame.locals import Rect

class Ball( Rect ):
    def __init__(self, surface, color=(180, 180, 180),\
                        diameter=20, speed=10, start=(300,300)):
        self.surface = surface
        self.COLOR = color
        self.SPEED = speed
        ANGLE = 30
        self.dir = randint(ANGLE, 180 - ANGLE)
        self.left = start[0]
        self.top = start[1]
        self.width = diameter
        self.height = diameter

    def stop_ball(self):
        self.SPEED = 0

    def movex(self):
        self.centerx += int( cos(radians(self.dir)) * self.SPEED )

    def movey(self):
        self.centery += int( sin(radians(self.dir)) * self.SPEED )

    def movexy(self):
        self.movex()
        self.movey()

    def draw(self):
        pygame.draw.ellipse(self.surface, self.COLOR, self)

