import pygame
from Assets.Menu_set import *
from Module.Options import *
from Module.Button import *

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.logo = pygame.image.load(Menu_path['logo_game'])
        self.logo_rect = self.logo.get_rect(center=(310, 75))
        self.click_sound = pygame.mixer.Sound(Menu_path['sound_klik'])
        self.startbuttons = Button(self.surface, (310, 200), "START")
        self.optbutton = Button(self.surface, (310, 260), "OPTIONS")
        self.quit = Button(self.surface, (310, 320), "QUIT")
    
    def cek_button(self, pointer):
        if self.startbuttons.input(pointer):
            self.click_sound.play()
            return self.startbuttons.input(pointer)
        if self.optbutton.input(pointer):
            self.click_sound.play()
        if self.quit.input(pointer):
            pygame.quit()
    
    def draw(self, pointer):
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)
        self.startbuttons.hover(pointer)
        self.startbuttons.update()
        self.optbutton.hover(pointer)
        self.optbutton.update()
        self.quit.hover(pointer)
        self.quit.update()