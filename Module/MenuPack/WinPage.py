from Assets.Settings import WIDTH
from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.layoutMenuPath import *

import pygame

class WinPage(Menu):
    def __init__(self, surface, nextlevel):
        super().__init__(surface)

        self.nextlevel = nextlevel 

        # font
        self.font = pygame.font.Font(layoutMenuPath['font'], 30)


        # text
        self.text = "You Won"
        self.textrender = self.font.render(self.text, True, (255, 255, 255))
        self.textrect = self.textrender.get_rect(center=(WIDTH/2, 75))
        self.leveltext = self.font.render("New Level Unlocked", True, (255, 255, 255))
        self.leveltextrect = self.leveltext.get_rect(center=(WIDTH/2, 125))
    
    def draw(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.textrender, self.textrect)
        self.surface.blit(self.leveltext, self.leveltextrect)