import pygame
from ..Entity import Entity

class Player(Entity):
    def __init__(self, pos, size):
        super().__init__(100, 10, 4, pos, size)
        self.image.fill('red')
        self.gravity = 0.5
        self.jump_speed = -8

    
    def get_input(self):
        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_a]:
            self.move(-1)
        elif self.keys[pygame.K_d]:
            self.move(1)
        else:
            self.move(0)
        
        if self.keys[pygame.K_w]:
            if self.pos.y == 0:
                self.jump()
    
    def move(self, x):
        self.pos.x = x
        self.rect.x += self.pos.x * self.speed

    def jump(self):
        self.pos.y = self.jump_speed
    
    def cek_gravity(self):

        self.pos.y += self.gravity
        self.rect.y += self.pos.y


    def update(self):
        self.get_input()
        
        self.cek_gravity()
        