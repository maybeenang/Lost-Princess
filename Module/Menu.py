import pygame
from Assets.Menu_set import *

class Menu:
    def __init__(self, surface):
        # window
        self.surface = surface
        # click sound
        self.click_sound = pygame.mixer.Sound(Menu_path['sound_klik'])
    
    def cek_button(self, pointer):
        pass
    
    def draw(self, pointer):
        pass
