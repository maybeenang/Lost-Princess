from Module.Menu import *
from Module.MenuPack.MainMenu import *
from Module.MenuPack.OptionMenu import *
import pygame

class MenuManager(Menu):
    def __init__(self, surface):
        super().__init__(surface)

        # backsound menu
        self.bg_sound = pygame.mixer.Sound(Menu_path['sound_bg'])
        self.soundstatus = 0.1
        self.bg_sound.set_volume(self.soundstatus)
        self.bg_sound.play(-1)

        self.mainmenu = MainMenu(self.surface, self.createoption, self.createlevelselect)
        
        self.status = 'main'
    
    def createoption(self):
        self.option = OptionMenu(self.surface, self.createmainmenu, self.soundstatus)
        self.status = 'opt'
    
    def createmainmenu(self):
        self.mainmenu = MainMenu(self.surface, self.createoption, self.createlevelselect)
        self.status = 'main'
    
    def createlevelselect(self):
        self.levelselect = LevelMenu(self.surface, self.createmainmenu)
        self.status = 'level'
    
    def set_sound(self):
        self.bg_sound.set_volume(self.soundstatus)
    
    def draw(self):

        self.set_sound()

        if self.status == 'main':
            self.mainmenu.draw()
        elif self.status == 'opt':
            self.option.draw()
            self.soundstatus = self.option.soundstatus
        elif self.status == 'level':
            self.levelselect.draw()
        # print(self.status)