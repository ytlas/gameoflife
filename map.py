class Map (object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        Matrix = [[0 for x in range(self.width/10)] for x in range(self.height/10)]
