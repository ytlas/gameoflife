#!/usr/bin/env python2
import pygame
import sys
from eventhandler import EventHandler
from map import Map

class Game(object):
    def __init__(self):
        pygame.init()
        self.width = 300
        self.height = 300
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.map = Map(width=self.width,height=self.height)
        while True:
            self.clock.tick(15)
            self.update()
            self.draw()
            EventHandler.handle_events()
    def update(self):
        pass
    def draw(self):
        self.window.fill((255, 0, 0))
        pygame.display.flip()

gof = Game()
