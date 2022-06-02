import pygame
import sys
from Assets.Settings import *
from Assets.Level_set import *
from Module.Level import *
from Module.MenuPack.MenuManager import *
from Assets.layoutMenuPath import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Lost Princess")

        # window yang digunakan
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # FPS
        self.__clock = pygame.time.Clock()

        # setup level
        self._maxlevel = 1

        # setup menu utama
        self.menu = MenuManager(self.screen, self.createlevel, self._maxlevel)

        # perkondisian 
        self.__status = 'menu'
        self.run()
    
    # membuat level
    def createlevel(self, currentlevel):
        self.level = Level(currentlevel, self.screen, self.createmenu, self._maxlevel)
        self.__status = 'game'

    # membuat menu
    def createmenu(self, newmaxlevel):
        if newmaxlevel > self._maxlevel:
            self._maxlevel = newmaxlevel
        self.menu = MenuManager(self.screen, self.createlevel, self._maxlevel)
        self.__status = 'menu'

    
    # event ketika ada sesuatu ketika game berjalan
    def events(self):
        for event in pygame.event.get():

            # jika tombol close ditekan
            if event.type == pygame.QUIT:
                sys.exit()
            
    # menampilkan menu yang dipilih  
    def drawmenu(self):
        self.menu.draw()
    
    # menampilkan level yang dipilih
    def drawlevel(self):
        self.screen.fill('black')
        self.level.draw()

    # ketika game sedang berjalan
    def run(self):
        while True:
            self.events()
            if self.__status == 'menu':
                self.drawmenu()

            elif self.__status == 'game':
                self.drawlevel()


            pygame.display.update()
            self.__clock.tick(FPS)