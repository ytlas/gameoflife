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
                mpos=pygame.mouse.get_pos()
                x=mpos[0]-(mpos[0]%10)
                y=mpos[1]-(mpos[1]%10)
                print(str(x)+" "+str(y))
