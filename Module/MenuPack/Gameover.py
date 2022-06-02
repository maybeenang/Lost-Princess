from Assets.Settings import WIDTH
from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.layoutMenuPath import *

import pygame

class Gameover(Menu):
    def __init__(self, surface, mainmenu, setstatus, oldmaxlevel, createlevelagain):
        super().__init__(surface)

        self.createmainmenu = mainmenu
        self.setstatus = setstatus
        self.oldmaxlevel = oldmaxlevel
        self.createlevelagain = createlevelagain

        # font
        self.font = pygame.font.Font(layoutMenuPath['font'], 30)

        # text
        self.text = "Game Over"
        self.textrender = self.font.render(self.text, True, (255, 255, 255))
        self.textrect = self.textrender.get_rect(center=(WIDTH/2, 75))

        self.currentbutton = 0
    
        # button
        self.resume = Button(self.surface, (WIDTH/2, 200), "Retry", 0)
        self.mainmenu = Button(self.surface, (WIDTH/2, 260), "Main Menu", 1)

        # # sound click
        self.soundclick = pygame.mixer.Sound(soundPath['click'])
        self.soundclicked = [
            pygame.mixer.Sound(soundPath['positive_click']), 
            pygame.mixer.Sound(soundPath['negative_click']), 
            pygame.mixer.Sound(soundPath['error_click'])
        ]

        # time
        self.time = pygame.time.get_ticks()
        self.delay = 200

    def input(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 0:
                self.currentbutton = 0
            else:
                self.soundclick.play()
                self.currentbutton -= 1
        elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 1:
                self.currentbutton = 1
            else:
                self.soundclick.play()
                self.currentbutton += 1
        
        if keys[pygame.K_ESCAPE] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            self.soundclicked[0].play()
            self.setstatus("running")

        
        if (keys[pygame.K_SPACE] or keys[pygame.K_RETURN]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 0:
                self.soundclicked[0].play()
                self.createlevelagain(3)
            elif self.currentbutton == 1:
                self.soundclicked[1].play()
                self.createmainmenu(self.oldmaxlevel)
    
    def draw(self):
        self.surface.blit(self.textrender, self.textrect)
        self.resume.update(self.currentbutton, "positive")
        self.mainmenu.update(self.currentbutton, "positive")