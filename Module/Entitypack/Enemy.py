import pygame
from Module.Entity import Entity
from Assets.Level_set import LEVEL_IMG
from Assets.Tools import importanimation

class Enemy(Entity):
    def __init__(self, pos, size):
        super().__init__(100, 50, 1, pos, size)
        self.importimage()
        self.index = 0
        self.indexspeed = 0.5
        self.image = self.animation["run"][self.index]
        self.status = "run"
    
    # import animasi perframe ke sebuah list
    def importimage(self):
        playerpath = LEVEL_IMG['enemy']
        self.animation = {
            "run": []
        }
        for animation in self.animation:
            fullpath = playerpath + animation
            self.animation[animation] = importanimation(fullpath)
    
    def animate(self):
        self.index += self.indexspeed
        if self.index >= len(self.animation[self.status]):
            self.index = 0
        self.image = self.animation[self.status][int(self.index)]

    
    def update(self, x_shift):
        self.animate()
        self.rect.x += x_shift