from Module.Item import Item
from Assets.Level_set import *
import pygame

class Bendera(Item):
    def __init__(self, pos, size, type):
        super().__init__(pos, size)

        if type == "merah":
            self.image =  pygame.image.load(LEVEL_IMG['benderamerah']).convert_alpha()
        elif type == "biru":
            self.image = pygame.image.load(LEVEL_IMG['benderabiru']).convert_alpha()
        
        self.rect = self.image.get_rect(center = pos)