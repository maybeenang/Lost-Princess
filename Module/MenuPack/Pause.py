from Assets.Settings import WIDTH
from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.layoutMenuPath import *

import pygame

class Pause(Menu):
    def __init__(self, surface, mainmenu, setstatus):
        super().__init__(surface)

        self.createmainmenu = mainmenu
        self.setstatus = setstatus

        # font
        self.font = pygame.font.Font(layoutMenuPath['font'], 30)

        # text
        self.text = "Game Paused"
        self.textrender = self.font.render(self.text, True, (255, 255, 255))
        self.textrect = self.textrender.get_rect(center=(WIDTH/2, 75))

        self.currentbutton = 0
    
        # button
        self.resume = Button(self.surface, (WIDTH/2, 200), "Resume", 0)
        self.mainmenu = Button(self.surface, (WIDTH/2, 260), "Main Menu", 1)

        # time
        self.time = pygame.time.get_ticks()
        self.delay = 200

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 0:
                self.currentbutton = 0
            else:
                self.currentbutton -= 1
        elif keys[pygame.K_s] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 1:
                self.currentbutton = 1
            else:
                self.currentbutton += 1
        
        if keys[pygame.K_RETURN] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 0:
                self.setstatus("running")
            elif self.currentbutton == 1:
                self.createmainmenu()
    
    def draw(self):
        self.surface.blit(self.textrender, self.textrect)
        self.resume.update(self.currentbutton)
        self.mainmenu.update(self.currentbutton)

    


