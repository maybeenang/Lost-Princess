from Assets.Settings import WIDTH
from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.Level_set import *
import pygame

class LevelMenu(Menu):
    def __init__(self, surface, back, createlevel, stopsound, maxlevel):
        super().__init__(surface)

        # logo di atas
        self.logo = self.font.render("Level Select", True, "white")
        self.logo_rect = self.logo.get_rect(center=(WIDTH/2, 50))

        # setup button
        self.maxlevel = maxlevel
        self.currentbutton = 0
        self.buttons = {}
        for level in LEVEL_SET:
            if level == 0:
                self.buttons[level] = Button(self.surface, (WIDTH/2, 200 + (level-1)*60), "Tutorial", level)
            else:
                self.buttons[level] = Button(self.surface, (WIDTH/2, 200 + (level-1)*60), "Level " + str(level), level)
            
            # ketika level belum di unlock
            if level > self.maxlevel:
                self.buttons[level].image = pygame.image.load(Menu_path['frame_tombol_negative'])
        
        # back button
        self.buttons[len(LEVEL_SET)] = Button(self.surface, (WIDTH/2, 200 + (len(LEVEL_SET)-1)*60), "Back", len(LEVEL_SET))
        
        # kembali ke main menu
        self.back = back

        # level saat ini
        self.createlevel = createlevel
        self.stopsound = stopsound

        # sound click
        self.soundclick = pygame.mixer.Sound(Menu_path['sound_klik'])
        self.soundclicked = [
            pygame.mixer.Sound(Menu_path['positive_click']), 
            pygame.mixer.Sound(Menu_path['negative_click']), 
            pygame.mixer.Sound(Menu_path['error_click'])
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
                    if button == len(LEVEL_SET):
                        self.soundclicked[1].play()
                        self.back()
                    else:
                        if self.currentbutton > self.maxlevel:
                            self.soundclicked[2].play()
                        else:
                            self.soundclicked[0].play()
                            self.createlevel()
                            self.stopsound()
    

    def draw(self):
        self.input()
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)
        for level in self.buttons:
            self.buttons[level].update(self.currentbutton)