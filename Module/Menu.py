import pygame
# from pygame.mixer import Sound
from Assets.layoutMenuPath import *
from Assets.soundPath import *



class Menu:
    def __init__(self, surface):
        # window
        self.surface = surface
        # click sound
        # self.click_sound = pygame.mixer.Sound(soundPath['click'])
        self.font = pygame.font.Font(layoutMenuPath['font'], 30)
    
    def cek_button(self):
        pass
    
    def draw(self):
        pass