from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.Settings import *

class CreditsPage(Menu):
    def __init__(self, surface, menu):
        super().__init__(surface)

        self.frame = pygame.image.load(layoutMenuPath['framecredits']).convert_alpha()

        self.back = menu
        # sound click
        self.soundclick = pygame.mixer.Sound(soundPath['click'])
        self.soundclicked = [
            pygame.mixer.Sound(soundPath['positive_click']), 
            pygame.mixer.Sound(soundPath['negative_click']),
            pygame.mixer.Sound(soundPath['error_click'])
        ]
        
        # time
        self.time = pygame.time.get_ticks()
        self.delay = 200
    
    def input(self):
        keys = pygame.key.get_pressed()
        
        if (keys[pygame.K_SPACE] or keys[pygame.K_RETURN]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            self.soundclicked[0].play()
            self.back()

    def draw(self):
        self.input()
        self.surface.blit(self.bg, (0, 0))
        self.surface.blit(self.frame, (0, 0))
