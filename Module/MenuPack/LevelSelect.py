from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.Level_set import *
import pygame

class LevelSelect(Menu):
    def __init__(self, surface):
        super().__init__(surface)
        self.logo = self.font.render("Level Select", True, "white")
        self.logo_rect = self.logo.get_rect(center=(310, 50))
        self.currentbutton = 0
        self.buttons = {}
        for level in LEVEL_SET:
            self.buttons[level] = Button(self.surface, (310, 200 + (level-1)*60), str(level), level)
        self.buttons[len(LEVEL_SET)] = Button(self.surface, (310, 200 + (len(LEVEL_SET)-1)*60), "Back", len(LEVEL_SET))
    
    def draw(self):
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)
        for level in self.buttons:
            self.buttons[level].update(self.currentbutton)