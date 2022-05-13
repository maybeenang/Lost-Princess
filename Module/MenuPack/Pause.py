from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.Menu_set import *

import pygame

class Pause(Menu):
    def __init__(self, surface):
        super().__init__(surface)

        # font
        self.font = pygame.font.Font(Menu_path['font'], 30)

        # text
        self.text = "Game Paused"
        self.textrender = self.font.render(self.text, True, (255, 255, 255))
        self.textrect = self.textrender.get_rect(center=(310, 75))
    
        # button
        self.resume = Button(self.surface, (310, 200), "Resume")
        self.mainmenu = Button(self.surface, (310, 260), "Main Menu")
    
    def cek_button(self, pointer):
        if self.resume.input(pointer):
            return 'resume'
        elif self.mainmenu.input(pointer):
            return 'quit'
    
    def draw(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.textrender, self.textrect)
        self.resume.update(pygame.mouse.get_pos())
        self.mainmenu.update(pygame.mouse.get_pos())

