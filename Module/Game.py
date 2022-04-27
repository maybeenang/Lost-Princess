import pygame
import sys
from Assets.Settings import *
from Assets.Level_set import *
from Module.Level import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level(LEVEL_1, self.screen)
        self.running = True
        self.run()
    
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
    
    def draw(self):
        self.screen.fill('black')
        self.level.draw()
        pygame.display.update()
        

    def run(self):
        while self.running:
            self.events()

            self.draw()
            self.clock.tick(FPS)
