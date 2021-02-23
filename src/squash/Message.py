import pygame

class Mess:
    def __init__(self, surface, size=80, color=(255,255,0)):
        self.surface = surface
        self.SIZE = size
        self.COLOR = color
        self.font = pygame.font.Font(None, size)
        self.MESSAGE = 'Hello'
        self.XPOS = self.YPOS = 0

    def display(self):
        text = self.font.render(self.MESSAGE, True, self.COLOR)
        textpos = text.get_rect()
        textpos.centerx = self.XPOS
        textpos.centery = self.YPOS
        self.surface.blit(text, textpos)

class Message( Mess ):
    def __init__(self, surface, message, xpos, ypos, size=80, color=(0,0,0)):
        super().__init__(surface, size, color)
        self.MESSAGE = message
        self.XPOS = xpos
        self.YPOS = ypos

