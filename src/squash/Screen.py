import pygame

class Screen:
    def __init__(self, width=600, height=600):
        self.WIDTH = width
        self.HEIGHT = height
        SIZE = (width, height)
        self.surface = pygame.display.set_mode( SIZE )

    def fill(self, color=(255, 255, 255)):
        self.surface.fill( color )

    def caption(self, str):
        pygame.display.set_caption( str )
