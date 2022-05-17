import pygame
from ..Entity import Entity

class Player(Entity):
    def __init__(self, pos, size, img):
        super().__init__(1000, 10, 4, pos, size)
        self.image = img
        # self.image.fill((255, 255, 255))
        self.health_now = 200
        self.max_health_bar = 400 
        self.health_ratio = self.health / self.max_health_bar
        self.gravity = 0.5
        self.jump_speed = -8
    
    def get_health(self, health):
        if self.health_now < self.health:
            self.health_now += health
        elif self.health_now > self.health:
            self.health_now = self.health
    
    def get_dmg(self, dmg):
        if self.health_now > 0:
            self.health_now -= dmg
        elif self.health_now <= 0:
            self.health_now = 0
    
    def health_bar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (5, 5, self.health_now / self.health_ratio, 25))
        pygame.draw.rect(screen, (0, 255, 0), (5, 5, self.max_health_bar, 25), 1)

    
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
        