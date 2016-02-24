import pygame
import sys

#Game file poop FUCK ADAM

class Game(object):

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        while True:
            self.clock.tick(15)
            self.update()
            self.draw()


    def update(self):
        pass

    def draw(self):
        self.window.fill((255, 0, 0))
        pygame.display.flip()

gof = Game()
