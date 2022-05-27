from Module.Item import Item
from Assets.Level_set import *
import pygame

class Bendera(Item):
    def __init__(self, x, y, size, type):
        super().__init__((x, y), size)

        if type == "merah":
            self.image =  pygame.image.load(LEVEL_IMG['benderamerah']).convert_alpha()
        elif type == "biru":
            self.image = pygame.image.load(LEVEL_IMG['benderabiru']).convert_alpha()
        
        self.rect.topleft = (x, y - 64)