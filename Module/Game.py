import pygame
import sys
from Assets.Settings import *
from Assets.Level_set import *
from Module.Level import *
from Module.MenuPack.MainMenu import *
from Module.MenuPack.Options import *
from Assets.Menu_set import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level(LEVEL_1, self.screen)
        self.menu = MainMenu(self.screen)
        self.opt = Options(self.screen)

        self.running = True
        self.cek_menu = True
        self.submenu = 'main'
        self.run()
    
    
    def events(self):
        pointer = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer = pygame.mouse.get_pos()

                if self.submenu == 'main':
                    if self.menu.cek_button(pointer) == 'start':
                        self.cek_menu = False
                    elif self.menu.cek_button(pointer) == 'opt':
                        self.submenu = 'opt'
                    elif self.menu.cek_button(pointer) == False:
                        self.running = False
                        sys.exit()

                elif self.submenu == 'opt':
                    if self.opt.cek_button(pointer) == 'back':
                        self.submenu = 'main'

    def drawmenu(self):
        if self.submenu == 'main':
            self.menu.draw()
        elif self.submenu == 'opt':
            self.opt.draw()
    
    def draw(self):
        self.screen.fill('grey')
        self.level.draw()
        if self.level.player.sprite.health <= 0:
            self.cek_menu = True

    def run(self):
        while self.running:
            self.events()

            if self.cek_menu:
                self.drawmenu()
            else:
                #self.bg_sound.fadeout(1000)
                self.draw()

            pygame.display.update()
            self.clock.tick(FPS)
