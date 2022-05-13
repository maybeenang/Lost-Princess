from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.Menu_set import *
import pygame

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

        # main menu button
        self.start = Button(self.surface, (310, 200), "START")
        self.opt = Button(self.surface, (310, 260), "OPTIONS")
        self.quit = Button(self.surface, (310, 320), "QUIT")

        # option button
        self.optlogo = pygame.image.load(Menu_path['optlogo'])
        self.optlog_rect = self.optlogo.get_rect(center=(310, 50))
        self.sound_button_on = Button(self.surface, (310, 200), "Sound: On")
        self.sound_button_off = Button(self.surface, (310, 200), "Sound: Off")
        self.back_button = Button(self.surface, (310, 312), "Back")
        self.optbutton = [self.sound_button_on, self.sound_button_off]
        
        # radiobutton
        self.index = 1

    def cek_button(self, pointer):

        if self.status == 'main':
            if self.start.input(pointer):
                self.click_sound.play()
                return 'start'
            elif self.opt.input(pointer):
                self.click_sound.play()
                return 'opt'
            elif self.quit.input(pointer):
                self.click_sound.play()
                return False

        elif self.status == 'opt':
            if self.back_button.input(pointer):
                self.click_sound.play()
                return 'backopt'
            # cek sound button
            if self.index == 0:
                if self.sound_button_on.input(pointer):
                    self.click_sound.play()
                    self.index = 1
                    self.bg_sound.play(-1)
                    return 'sound_off'
            elif self.index == 1:
                if self.sound_button_off.input(pointer):
                    self.click_sound.play()
                    self.index = 0
                    self.bg_sound.stop()
                    return 'sound_on'
                
    
    def draw(self):
        pointer = pygame.mouse.get_pos()
        self.surface.fill('grey')

        if self.status == 'main':
            self.surface.blit(self.logo, self.logo_rect)
            self.start.update(pointer)
            self.opt.update(pointer)
            self.quit.update(pointer)

        elif self.status == 'opt':
            self.surface.blit(self.optlogo, self.optlog_rect)
            self.optbutton[self.index].update(pointer)
            self.back_button.update(pointer)

