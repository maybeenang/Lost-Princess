from email.mime import image
from Module.Item import Item
from Assets.Level_set import *
from Assets.Tools import *
import pygame

class Particle(Item):
    def __init__(self, pos, type):
        super().__init__(pos, 10)

        self.type = type
        if self.type == "jump":
            self.frame = importanimation(LEVEL_IMG['particlejump'])
        if self.type == "land":
            self.frame = importanimation(LEVEL_IMG['particleland'])
        if self.type == "explosion":
            self.frame = importanimation(LEVEL_IMG['particleexplosion'])
        if self.type == "kill":
            self.frame = importanimation(LEVEL_IMG['particlekill'])
        self.index = 0
        self.index_speed = 0.5
        self.image = self.frame[self.index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.index += self.index_speed
        if self.index >= len(self.frame):
            self.kill()
        else:
            self.image = self.frame[int(self.index)]

    def update(self, x):
        self.rect.x += x
        self.animate()


