import pygame
from Assets.Menu_set import *
from Module.Button import *
from Module.Menu import *

class Options:
    def __init__(self, surface):
        self.surface = surface
        self.optlogo = pygame.image.load(Menu_path['optlogo'])
        self.b_f = pygame.image.load(Menu_path['frame_tombol'])
        self.c_s = pygame.mixer.Sound(Menu_path['sound_klik'])
        self.optlog_rect = self.optlogo.get_rect(center=(310, 50))
        self.sound_button_on = Button(self.surface, (310, 200), "Sound: On")
        self.sound_button_off = Button(self.surface, (310, 200), "Sound: Off")
        self.back_button = Button(self.surface, (310, 312), "Back")
        self.optbutton = [self.sound_button_on, self.back_button]

    def cek(self, pointer):
        pointer = pygame.mouse.get_pos()
        return self.back_button.input(pointer)

    def draw(self, pointer):
        self.surface.fill('black')
        self.surface.blit(self.optlogo, self.optlog_rect)
        for i in self.optbutton:
            i.hover(pointer)
            i.update()