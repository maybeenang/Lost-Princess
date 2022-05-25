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

        # window yang digunakan
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # FPS
        self.clock = pygame.time.Clock()

        # setup level
        self.maxlevel = 1

        # setup menu utama
        self.menu = MenuManager(self.screen, self.createlevel, self.maxlevel)

        # perkondisian
        self.status = 'menu'
        self.run()
    
    # membuat level
    def createlevel(self):
        self.level = Level(LEVEL_1, self.screen, self.createmenu)
        self.status = 'game'

    # membuat menu
    def createmenu(self):
        self.menu = MenuManager(self.screen, self.createlevel, self.maxlevel)
        self.status = 'menu'

    
    # event ketika ada sesuatu ketika game berjalan
    def events(self):
        for event in pygame.event.get():

            # jika tombol close ditekan
            if event.type == pygame.QUIT:
                sys.exit()
            
                    
    def drawmenu(self):
        self.menu.draw()
        # self.menu.soundplay()
    
    def drawlevel(self):
        self.screen.fill('black')
        self.level.draw()

    def run(self):
        while True:
            self.events()
            if self.status == 'menu':
                self.drawmenu()

            elif self.status == 'game':
                self.drawlevel()

            else:
                #self.bg_sound.fadeout(1000)
                self.draw()


            pygame.display.update()
            self.clock.tick(FPS)