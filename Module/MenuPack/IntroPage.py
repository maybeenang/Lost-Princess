import pygame
from Assets.Menu_set import *
from Module.MenuPack.Button import *

class Intro:
    def __init__(self, surface):
        self.surface = surface
        self.logo_tim = pygame.image.load(Menu_path['logo_tim'])
        self.logo_tim_rect = self.logo_tim.get_rect(center=(310, 200))
        self.logo_game = pygame.image.load(Menu_path['logo_game'])
        self.logo_game_rect = self.logo_game.get_rect(center=(310, 200))
        self.running = True

    def draw_dev_logo(self):
        self.surface.fill('black')
        self.surface.blit(self.logo_tim, (0, 0))
        pygame.display.update()

    def draw_game_logo(self):
        self.surface.fill('black')
        self.surface.blit(self.logo_game, (0, 0))
        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.draw_dev_logo()
            self.draw_game_logo()
            self.running = False