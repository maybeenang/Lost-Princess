from Assets.Settings import WIDTH
from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.layoutMenuPath import *

import pygame

class DeathPage(Menu):
    def __init__(self, surface, setstatus, nyawa):
        super().__init__(surface)

        self.setstatus = setstatus
        self.nyawa = nyawa

        # font
        self.font = pygame.font.Font(layoutMenuPath['font'], 30)


        # text
        self.text = "You Death"
        self.textrender = self.font.render(self.text, True, (255, 255, 255))
        self.textrect = self.textrender.get_rect(center=(WIDTH/2, 75))
        self.heart = self.font.render("x" + str(self.nyawa - 1), True, (255, 255, 255))
        self.heartrect = self.heart.get_rect(center=(WIDTH/2, 125))
    
    def draw(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.textrender, self.textrect)
        self.surface.blit(self.heart, self.heartrect)