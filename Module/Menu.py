import pygame
from Assets.Menu_set import *
from Module.Button import *

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.bg = pygame.image.load(Menu_path['bg'])
        self.logo = pygame.image.load(Menu_path['logo_game'])
        self.logo_rect = self.logo.get_rect(center=(310, 75))
        self.backsound = pygame.mixer.Sound(Menu_path['sound_bg'])
        self.startbuttons = Button(self.surface, (310, 200), "Start")
        self.quit = Button(self.surface, (310, 280), "Quit")
    
    def cek_button(self, pointer):
        return self.startbuttons.input(pointer)
    
    def draw(self, pointer):
        self.backsound.play(-1)
        self.surface.fill('black')
        self.surface.blit(self.logo, self.logo_rect)
        self.startbuttons.hover(pointer)
        self.startbuttons.update()
        self.quit.hover(pointer)
        self.quit.update()