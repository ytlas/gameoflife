import pygame
from pygame.locals import *
import sys

class EventHandler(object):
    @classmethod
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
            
