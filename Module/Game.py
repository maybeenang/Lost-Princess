import pygame
import sys
from Assets.Settings import *
from Assets.Level_set import *
from Module.Level import *
from Module.MenuPack.MainMenu import *
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
        self.menu = MainMenu(self.screen)

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
            
            # jika salah satu tombol keyboard ditekan
            if event.type == pygame.KEYDOWN:
                
                # ketika berada di main menu
                if self.cek_menu:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        # ketika berada di menu utama
                        if self.menu.status == "main":
                            if self.menu.currentbutton >= len(self.menu.buttons) - 1:
                                self.menu.currentbutton = len(self.menu.buttons) - 1
                            else:
                                self.menu.currentbutton += 1
                        # ketika berada di menu option
                        elif self.menu.status == "opt":
                            if self.menu.currentoptbutton >= len(self.menu.optbutton)-1:
                                self.menu.currentoptbutton = len(self.menu.optbutton)-1
                            else:
                                self.menu.currentoptbutton += 1

                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        # ketika berada di menu utama
                        if self.menu.status == "main":
                            if self.menu.currentbutton == 0:
                                self.menu.currentbutton = 0
                            else:
                                self.menu.currentbutton -= 1
                        # ketika berada di menu option
                        elif self.menu.status == "opt":
                            if self.menu.currentoptbutton == 0:
                                self.menu.currentoptbutton = 0
                            else:
                                self.menu.currentoptbutton -= 1
                    
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                        self.menu.cek_button()
                    
    def drawmenu(self):
        self.menu.draw()
    
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
            # else:
            # self.menu.bg_sound.fadeout(1000)
                # self.draw()

            pygame.display.update()
            self.clock.tick(FPS)
