import pygame
from Assets.Menu_set import *

class Menu:
    def __init__(self, surface):
        # window
        self.surface = surface
        # click sound
        self.click_sound = pygame.mixer.Sound(Menu_path['sound_klik'])
        self.font = pygame.font.Font(Menu_path['font'], 30)
    
    def cek_button(self):
        pass
    
    def draw(self):
        pass