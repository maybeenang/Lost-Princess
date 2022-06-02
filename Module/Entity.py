import pygame

# parent class untuk entity
class Entity(pygame.sprite.Sprite):
    def __init__(self, health, damage, speed, pos, size):
        super().__init__()

        # atribut yang diperlukan sebagai entity
        self.health = health
        self.damage = damage
        self.speed = speed
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.pos = pygame.math.Vector2(0,0)
    
    # method untuk mengupdate posisi entity
    def move(self, x):
        pass