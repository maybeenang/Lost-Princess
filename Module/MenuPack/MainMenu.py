from Module.Menu import *
from Module.MenuPack.Button import *
from Module.MenuPack.LevelSelect import *
from Assets.Menu_set import *
import pygame, sys

class MainMenu(Menu):
    def __init__(self, surface):
        super().__init__(surface)

        # logo
        self.logo = pygame.image.load(Menu_path['logo_game'])
        self.logo_rect = self.logo.get_rect(center=(310, 75))

        # backsound menu
        self.bg_sound = pygame.mixer.Sound(Menu_path['sound_bg'])
        self.bg_sound.play(-1)

        # status
        self.status = 'main'
        self.currentbutton = 0
        self.currentoptbutton = 0

        # main menu button
        self.buttons = {
            'start': Button(self.surface, (310, 200), 'Start', 0),
            'opt': Button(self.surface, (310, 260), 'Option', 1),
            'quit': Button(self.surface, (310, 320), 'Quit', 2)
        }

        # option button
        self.optlogo = pygame.image.load(Menu_path['optlogo'])
        self.optlog_rect = self.optlogo.get_rect(center=(310, 50))
        self.soundstatus = "on"
        self.optbutton = {
            'back': Button(self.surface, (310, 200), 'Back', 0),
            'sound': Button(self.surface, (310, 260), 'Sound Off', 1)
        }

    def cek_button(self):
        if self.status == 'main':
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'start':
                        self.status = 'play'
                    elif button == 'opt':
                        self.status = 'opt'
                    elif button == 'quit':
                        self.running = False
                        sys.exit()
        elif self.status == 'opt':
            for button in self.optbutton:
                if self.optbutton[button].input(self.currentoptbutton):
                    if button == 'back':
                        self.currentoptbutton = 0
                        self.status = 'main'
                    elif button == 'sound':
                        print(self.soundstatus)
                        if self.soundstatus == "on":
                            self.soundstatus = "off"
                            self.optbutton[button].temp_text = 'Sound On'
                            self.bg_sound.stop()
                        elif self.soundstatus == "off":
                            self.soundstatus = "on"
                            self.optbutton[button].temp_text = 'Sound Off'
                            self.bg_sound.play(-1)
    
    def draw(self):
        self.surface.fill('grey')
        if self.status == 'main':
            self.surface.blit(self.logo, self.logo_rect)
            for button in self.buttons:
                self.buttons[button].update(self.currentbutton)
        elif self.status == 'opt':
            self.surface.blit(self.optlogo, self.optlog_rect)
            for button in self.optbutton:
                self.optbutton[button].update(self.currentoptbutton)
        elif self.status == 'play':
            levelselect = LevelSelect(self.surface)
            levelselect.draw()
