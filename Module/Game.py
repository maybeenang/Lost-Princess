import pygame
import sys
from Assets.Settings import *
from Assets.Level_set import *
from Module.Level import *
from Module.Menu import *
from Assets.Menu_set import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level(LEVEL_1, self.screen)
        self.menu = Menu(self.screen)
        self.running = True
        self.cek_menu = True
        self.run()
    
    
    def events(self):
        pointer = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and self.menu.cek_button(pointer):
                self.cek_menu = False
    
    def drawmenu(self):
        pointer = pygame.mouse.get_pos()
        self.menu.draw(pointer)

    
    def draw(self):
        self.screen.fill('grey')
        self.level.draw()
        if self.level.player.sprite.health <= 0:
            self.cek_menu = True

    def run(self):
        self.bg = pygame.mixer.Sound(Menu_path['sound_bg'])
        self.bg.play(-1)
        while self.running:
            self.events()

            if self.cek_menu:
                self.drawmenu()
            else:
                self.bg.fadeout(1000)
                self.draw()

            pygame.display.update()
            self.clock.tick(FPS)
