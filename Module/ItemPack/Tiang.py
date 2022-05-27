from Module.Item import Item
from Assets.Level_set import *
import pygame

class Tiang(Item):
    def __init__(self, x, y, size):
        super().__init__((x, y), size)
        self.image = pygame.image.load(LEVEL_IMG['tiang']).convert_alpha()
        
        self.rect.topleft = (x, y - 64)