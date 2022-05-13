from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.Menu_set import *
import pygame

class Options(Menu):
    def __init__(self, surface):
        super().__init__(surface)

        # component
        self.optlogo = pygame.image.load(Menu_path['optlogo'])
        self.optlog_rect = self.optlogo.get_rect(center=(310, 50))

        # radiobutton
        self.index = 0

        # button
        self.sound_button_on = Button(self.surface, (310, 200), "Sound: On")
        self.sound_button_off = Button(self.surface, (310, 200), "Sound: Off")

        self.back_button = Button(self.surface, (310, 312), "Back")
        self.optbutton = [self.sound_button_on, self.sound_button_off]

    def cek_button(self, pointer):
        if self.back_button.input(pointer):
            self.click_sound.play()
            return 'back'
        
        # cek sound button
        if self.index == 0:
            if self.sound_button_on.input(pointer):
                self.click_sound.play()
                self.index = 1
                return 'sound_on'
        elif self.index == 1:
            if self.sound_button_off.input(pointer):
                self.click_sound.play()
                self.index = 0
                return 'sound_off'


    def draw(self):
        self.surface.fill('black')
        self.surface.blit(self.optlogo, self.optlog_rect)

        self.optbutton[self.index].update(pygame.mouse.get_pos())
        self.back_button.update(pygame.mouse.get_pos())