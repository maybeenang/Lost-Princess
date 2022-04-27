import pygame
from ..Entity import Entity

class Enemy(Entity):
    def __init__(self, pos, size, img):
        super().__init__(100, 50, 1, pos, size)
        self.image = img