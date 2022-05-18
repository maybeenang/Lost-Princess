import pygame
import sys
from Assets.Settings import *
from Assets.Level_set import *
from Module.Level import *
from Module.MenuPack.MenuManager import *
from Assets.Menu_set import *

class Game:
    def __init__(self):
        pygame.init()

        # window yang digunakan
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # FPS
        self.clock = pygame.time.Clock()

        # setup level
        self.level = Level(LEVEL_1, self.screen)

        # setup menu utama
        self.menu = MenuManager(self.screen)

        # perkondisian
        self.running = True
        self.cek_menu = True
        self.run()
    
    # event ketika ada sesuatu ketika game berjalan
    def events(self):
        for event in pygame.event.get():

            # jika tombol close ditekan
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            
                    
    def drawmenu(self):
        self.menu.draw()
        # self.menu.soundplay()
    
    def draw(self):
        self.screen.fill('black')
        self.level.draw()
        if self.level.player.sprite.health <= 0:
            self.cek_menu = True

    def run(self):
        while self.running:
            self.events()
            if self.cek_menu:
                self.drawmenu()

            pygame.display.update()
            self.clock.tick(FPS)