from Assets.Settings import WIDTH
from Module.Item import Item
import pygame

class Background(Item):
    def __init__(self, pos, img):
        super().__init__(pos, 0)

        self.image = img