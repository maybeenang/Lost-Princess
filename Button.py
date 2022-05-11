import pygame
from Assets.Menu_set import *

class Button:
    def __init__(self, surface , pos, text):
        self.surface = surface
        self.font = pygame.font.Font(Menu_path['font'], 25)
        self.image = pygame.image.load(Menu_path['frame_tombol'])
        self.color = "#fde047"
        self.hover_color = "white"
        self.text = self.font.render(text, True, self.color)
        self.temp_text = text
        
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=pos)
        self.tect_rect = self.text.get_rect(center=pos)
    
    def input(self, mousepos):

        if mousepos[0] in range(self.rect.left, self.rect.right) and mousepos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def hover(self, mousepos):

        if mousepos[0] in range(self.rect.left, self.rect.right) and mousepos[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.temp_text, True, self.hover_color)
        else:
            self.text = self.font.render(self.temp_text, True, self.color)

    def update(self):
        if self.image is not None:
            self.surface.blit(self.image, self.rect)
        self.surface.blit(self.text, self.tect_rect)
