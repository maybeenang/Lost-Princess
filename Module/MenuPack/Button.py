import pygame
from Assets.layoutMenuPath import *

class Button:
    def __init__(self, surface , pos, text, index):

        # window
        self.surface = surface

        # component
        self.font = pygame.font.Font(layoutMenuPath['font'], 20)
        self.image = pygame.image.load(layoutMenuPath['tombolpositive'])
        self.color = "#363636"
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
    
    def hover(self, index, status):
        if self.index == index:
            if status == "positive":
                self.image = pygame.image.load(layoutMenuPath['tombolhover'])
            else:
                self.image = pygame.image.load(layoutMenuPath['tombolnegativehover'])
        else:
            if status == "positive":
                self.image = pygame.image.load(layoutMenuPath['tombolpositive'])
            else:
                self.image = pygame.image.load(layoutMenuPath['tombolnegative'])

    def update(self, index, status):
        self.hover(index, status)
        if self.image is not None:
            self.surface.blit(self.image, self.rect)
        self.surface.blit(self.text, self.tect_rect)