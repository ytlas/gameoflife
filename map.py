class Map (object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        grid = [[0 for x in range(self.width/10)] for x in range(self.height/10)]
    def draw(self,grid):
        pygame.draw.rect(self.window, BLACK, [0, 0, 10, 10])
