import pygame
# from pygame.mixer import Sound
from Assets.layoutMenuPath import *
from Assets.soundPath import *

# parent class untuk menu
class Menu:
    def __init__(self, surface):
        # window
        self.surface = surface
        
        # click sound
        self.click_sound = pygame.mixer.Sound(soundPath['click'])
        self.font = pygame.font.Font(layoutMenuPath['font'], 23)
        self.frame = pygame.image.load(layoutMenuPath['frame']).convert_alpha()
        self.bg = pygame.image.load(layoutMenuPath['bg']).convert_alpha()
    
    def draw(self):
        pass