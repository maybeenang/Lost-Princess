from Module.Menu import *
from Module.MenuPack.MainMenu import *
from Module.MenuPack.OptionMenu import *
from Assets.layoutMenuPath import *
from Assets.soundPath import *
import pygame

class MenuManager(Menu):
    def __init__(self, surface, level, maxlevel):
        super().__init__(surface)

        # backsound menu
        self.__bg_sound = pygame.mixer.Sound(soundPath['inmenubacksound'])
        self.soundstatus = 0.2
        self.__bg_sound.set_volume(self.soundstatus)
        self.__bg_sound.play(-1)
        self.mainmenu = MainMenu(self.surface, self.createoption, self.createlevelselect)

        # level status
        self._maxlevel = maxlevel
        self.level = level
        self.__status = 'main'
    
    def createoption(self):
        self.option = OptionMenu(self.surface, self.createmainmenu, self.soundstatus)
        self.__status = 'opt'
    
    def createmainmenu(self):
        self.mainmenu = MainMenu(self.surface, self.createoption, self.createlevelselect)
        self.__status = 'main'
    
    def createlevelselect(self):
        self.levelselect = LevelMenu(self.surface, self.createmainmenu, self.level, self.stopsound, self._maxlevel)
        self.__status = 'level'
    
    def set_sound(self):
        # pass
        self.__bg_sound.set_volume(self.soundstatus)
    
    def stopsound(self):
        # pass
        self.__bg_sound.stop()
    
    def draw(self):

        self.set_sound()

        if self.__status == 'main':
            self.mainmenu.draw()
        elif self.__status == 'opt':
            self.option.draw()
            self.soundstatus = self.option.soundstatus
        elif self.__status == 'level':
            self.levelselect.draw()
        # print(self.status)