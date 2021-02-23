import sys
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT
from random import randint
from Ball import Ball
from Message import Message
from Racket import Racket
from Screen import Screen

class Game():
    WHITE = (255, 255, 255)
    def __init__(self):
        pygame.init()
        self.WIDTH = 640
        self.HEIGHT = 480
        self.screen = Screen( self.WIDTH, self.HEIGHT)
        self.screen.caption("Squash game")
        self.clock = pygame.time.Clock()
        self.FPS = 30
        RED = (255,0,0)
        START = ( randint(0,self.WIDTH-1),0 )
        self.ball = Ball( self.screen.surface, color=RED, start=START )
        left = self.WIDTH//2
        top = self.HEIGHT - 50
        self.racket = Racket(self.screen.surface, left=left, top=top)
        xpos = left
        ypos = self.HEIGHT//2
        YELLOW = (255,255,0)
        self.msg_gover = Message( self.screen.surface, 'Game Over!!',\
                                  xpos, ypos, color=YELLOW )
        pygame.key.set_repeat(10, 10)

    def fine(self):
        pygame.quit()
        sys.exit()

    def key_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.fine()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and self.racket.left > 0:
                    self.racket.movex(-3)
                elif event.key == K_RIGHT and self.racket.right < self.WIDTH:
                    self.racket.movex(3)

    def hitted(self, racket, ball):
        if racket.colliderect( ball ):
            ball.dir = -(90+(racket.centerx-ball.centerx)/racket.width*100)

    def boundary(self, ball):
        if not (0 < ball.centerx < self.WIDTH):
            ball.dir = 180 - ball.dir
        if ball.centery < 0:
            ball.dir = -ball.dir
        if self.HEIGHT < ball.centery:
            ball.stop_ball()
            self.msg_gover.display()

    def start(self):
        game_over = False
        while not game_over:
            self.key_event()
            self.screen.fill( Game.WHITE )
            self.ball.draw()
            self.racket.draw()
            self.hitted( self.racket, self.ball )
            self.boundary( self.ball )
            self.ball.movexy()
            pygame.display.update()
            self.clock.tick(self.FPS)

