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

        # button
        self.start = Button(self.surface, (310, 200), "START")
        self.opt = Button(self.surface, (310, 260), "OPTIONS")
        self.quit = Button(self.surface, (310, 320), "QUIT")

    def cek_button(self, pointer):
        if self.start.input(pointer):
            self.click_sound.play()
            return 'start'
        elif self.opt.input(pointer):
            self.click_sound.play()
            return 'opt'
        elif self.quit.input(pointer):
            self.click_sound.play()
            return False
                
    
    def draw(self):

        pointer = pygame.mouse.get_pos()
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)
        self.start.update(pointer)
        self.opt.update(pointer)
        self.quit.update(pointer)

