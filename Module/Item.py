import pygame

# parent class untuk item
class Item(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()

        # atribut yang diperlukan sebagai item
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = pos)

    # method untuk mengupdate posisi item
    def update(self, x):
        self.rect.x += x