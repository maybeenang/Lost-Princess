import pygame
from Assets.Menu_set import *

class Button:
    def __init__(self, surface , pos, text, index):

        # window
        self.surface = surface

        # component
        self.font = pygame.font.Font(Menu_path['font'], 25)
        self.image = pygame.image.load(Menu_path['frame_tombol'])
        self.color = "#fde047"
        self.hover_color = "white"
        self.index = index

        # text
        self.temp_text = text
        self.text = self.font.render(self.temp_text, True, self.color)
        
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=pos)
        self.tect_rect = self.text.get_rect(center=pos)
    
    def input(self, index):
        if self.index == index:
            return True
        else:
            return False
    
    def hover(self, index):
        if self.index == index:
            self.text = self.font.render(self.temp_text, True, self.hover_color)
        else:
            self.text = self.font.render(self.temp_text, True, self.color)

    def update(self, index):
        self.hover(index)
        if self.image is not None:
            self.surface.blit(self.image, self.rect)
        self.surface.blit(self.text, self.tect_rect)