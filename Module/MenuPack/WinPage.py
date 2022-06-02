from Assets.Settings import HEIGHT, WIDTH
from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.layoutMenuPath import *

import pygame

class WinPage(Menu):
    def __init__(self, surface, nextlevel):
        super().__init__(surface)

        self.nextlevel = nextlevel 

        # font
        self.font = pygame.font.Font(layoutMenuPath['font'], 15)


        # text

        if self.nextlevel == 1:
            self.textatas = "You Won"
            self.textbawah = "You have finished the tutorial"
        elif self.nextlevel > 1 and self.nextlevel < 5:
            self.textatas = "You Won"
            self.textbawah = "You Unlocked The Next Level"
        elif self.nextlevel == 5:
            self.textatas = "Congratulations"
            self.textbawah = "You have successfully saved the princess"

        self.textrender = self.font.render(self.textatas, True, (255, 255, 255))
        self.textrect = self.textrender.get_rect(center=(WIDTH/2, HEIGHT/2 - 25))
        self.leveltext = self.font.render(self.textbawah, True, (255, 255, 255))
        self.leveltextrect = self.leveltext.get_rect(center=(WIDTH/2, HEIGHT/2))
    
    def draw(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.textrender, self.textrect)
        self.surface.blit(self.leveltext, self.leveltextrect)