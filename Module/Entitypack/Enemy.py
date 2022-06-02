import pygame
from random import randint
from Module.Entity import Entity
from Assets.Level_set import LEVEL_IMG
from Assets.Tools import importanimation

class Enemy(Entity):
    def __init__(self, pos, size):
        super().__init__(100, 50, randint(3, 5), pos, size)
        self.importimage()
        self.index = 0
        self.indexspeed = 0.5
        self.image = self.animation["run"][self.index]
        self.status = "run"

    def move(self):
        self.rect.x += self.speed
        
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

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def reverse(self):
        self.speed *= -1

    
    def update(self, x_shift):
        self.rect.x += x_shift
        self.animate()
        self.move()
        self.reverse_image()