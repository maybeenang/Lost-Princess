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
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level(LEVEL_1, self.screen)
        self.menu = MainMenu(self.screen)

        self.running = True
        self.cek_menu = True
        self.run()
    
    
    def events(self):
        pointer = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not self.cek_menu:
                        if self.level.status:
                            self.level.status = False
                        else:
                            self.level.status = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pointer = pygame.mouse.get_pos()
                if self.menu.status == 'main':
                    if self.menu.cek_button(pointer) == 'start':
                        self.cek_menu = False
                    elif self.menu.cek_button(pointer) == 'opt':
                        self.menu.status = 'opt'
                    elif self.menu.cek_button(pointer) == False:
                        self.running = False
                        sys.exit()
                elif self.menu.status == 'opt':
                    if self.menu.cek_button(pointer) == 'backopt':
                        self.menu.status = 'main'
                
                if not self.cek_menu:
                    if self.level.status == 'running':
                        if self.level.pause_game(pointer):
                            self.level.status = 'pause'
                    else:
                        if self.level.pause.cek_button(pointer) == 'resume':
                            self.level.status = 'running'
                        elif self.level.pause.cek_button(pointer) == 'quit':
                            self.menu.status = 'main'
                            self.cek_menu = True

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
            else:
                self.menu.bg_sound.fadeout(1000)
                self.draw()

            pygame.display.update()
            self.clock.tick(FPS)
