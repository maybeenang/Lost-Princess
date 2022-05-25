from Assets.Settings import WIDTH
from Module.Menu import *
from Module.MenuPack.Button import *
from Module.MenuPack.LevelMenu import *
from Module.MenuPack.OptionMenu import *
from Assets.layoutMenuPath import *
from Assets.soundPath import *
import pygame, sys

class MainMenu(Menu):
    def __init__(self, surface, opt, level):
        super().__init__(surface)

        # logo
        self.font = pygame.font.Font(layoutMenuPath['font'], 40)
        self.logo = self.font.render("Lost Princess", True, "white")
        self.logo_rect = self.logo.get_rect(center=(WIDTH/2, 100))

        # status
        self.currentbutton = 0
        self.opt = opt
        
        self.level = level

        # main menu button
        self.buttons = {
            'start': Button(self.surface, (WIDTH/2, 160), 'Start', 0),
            'opt': Button(self.surface, (WIDTH/2, 220), 'Option', 1),
            'quit': Button(self.surface, (WIDTH/2, 280), 'Quit', 2)
        }

        # sound click
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
        if keys[pygame.K_s] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == len(self.buttons) - 1:
                self.currentbutton = len(self.buttons)-1
            else:
                self.soundclick.play()
                self.currentbutton += 1
        elif keys[pygame.K_w] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 0:
                self.currentbutton = 0
            else:
                self.soundclick.play()
                self.currentbutton -= 1
        
        if keys[pygame.K_SPACE] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'start':
                        self.soundclicked[0].play()
                        self.level()
                    elif button == 'opt':
                        self.soundclicked[0].play()
                        self.opt()
                    elif button == 'quit':
                        self.soundclicked[1].play()
                        pygame.quit()
                        sys.exit()
    
    
    def draw(self):
        self.input()
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)
        for button in self.buttons:
            self.buttons[button].update(self.currentbutton)
