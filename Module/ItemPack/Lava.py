from Module.Item import Item
from Assets.Level_set import *
from Assets.Tools import *

class Lava(Item):
    def __init__(self, x, y, size):
        super().__init__((x, y), size)

        self.frame = importanimation(LEVEL_IMG['lava'])
        self.index = 0
        self.index_speed = 0.15
        self.image = self.frame[self.index]
        self.rect = self.image.get_rect(topleft = (x, y))
    
    def animate(self):
        self.index += self.index_speed
        if self.index >= len(self.frame):
            self.index = 0
        else:
            self.image = self.frame[int(self.index)]
    
    def update(self, x):
        self.rect.x += x
        self.animate()