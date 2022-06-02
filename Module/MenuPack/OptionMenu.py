from Module.Menu import *
from Module.MenuPack.Button import *
from Assets.Settings import *

class OptionMenu(Menu):
    def __init__(self, surface, menu, soundstatus):
        super().__init__(surface)

        self.logo = self.font.render("Option", True, "#e3b616")
        self.logo_rect = self.logo.get_rect(center=(WIDTH/2, 71))
        self.frame = pygame.image.load(layoutMenuPath['frameoption']).convert_alpha()
        self.__currentbutton = 0
        self.createmenu = menu

        # sound click
        self.soundclick = pygame.mixer.Sound(soundPath['click'])
        self.soundclicked = [
            pygame.mixer.Sound(soundPath['positive_click']), 
            pygame.mixer.Sound(soundPath['negative_click']),
            pygame.mixer.Sound(soundPath['error_click'])
        ]
        

        self.soundstatus = soundstatus
        self.buttons = {
            'back': Button(self.surface, (WIDTH/2, 200), 'Back', 0),
            'sound': Button(self.surface, (WIDTH/2, 320), 'Sound', 1)
        }

        # volume slider
        self.currentvolume = self.soundstatus * 1000
        self.maxvolume = 1000
        self.volumelenght = 300
        self.volumeratio = self.maxvolume / self.volumelenght

        # time
        self.time = pygame.time.get_ticks()
        self.delay = 200
    
    def input(self):
        keys = pygame.key.get_pressed()

        # vertical input
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.__currentbutton == len(self.buttons) - 1:
                self.__currentbutton = len(self.buttons)-1
            else:
                self.soundclick.play()
                self.__currentbutton += 1
        elif (keys[pygame.K_UP] or keys[pygame.K_w]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.__currentbutton == 0:
                self.__currentbutton = 0
            else:
                self.soundclick.play()
                self.__currentbutton -= 1
        
        # horizontal input
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.__currentbutton):
                    if button == 'sound':
                        if self.soundstatus < 1.0:
                            self.soundstatus += 0.2
                        elif self.soundstatus == 1.0:
                            self.soundstatus = 1.0
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.__currentbutton):
                    if button == 'sound':
                        if self.soundstatus > 0.0:
                            self.soundstatus -= 0.2
                        elif self.soundstatus == 0:
                            self.soundstatus = 0.0
        
        if keys[pygame.K_ESCAPE] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            self.soundclicked[0].play()
            self.createmenu()

        if (keys[pygame.K_SPACE] or keys[pygame.K_RETURN]) and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.__currentbutton):
                    if button == 'back':
                        self.soundclicked[0].play()
                        self.createmenu()
                    elif button == 'sound':
                        # pass
                        self.soundclicked[2].play()
                        # self.soundstatus(0.0)
    
    def cekvolumebar(self):
        if int(self.currentvolume) < self.maxvolume:
            self.currentvolume = self.soundstatus * 1000
        else:
            self.currentvolume = self.maxvolume 

        if int(self.currentvolume) > 0:
            self.currentvolume = self.soundstatus * 1000
        else:
            self.currentvolume = 0

    def soundbar(self):
        self.value = pygame.draw.rect(self.surface, 'green', (WIDTH/4 + 26, 380, self.currentvolume / self.volumeratio, 20), border_radius=8)
        self.border = pygame.draw.rect(self.surface, 'black', (WIDTH/4 + 26, 380, self.volumelenght, 20), 3, 8)

    def draw(self):
        self.input()
        self.surface.blit(self.bg, (0, 0))
        self.surface.blit(self.frame, (0, 0))
        self.surface.blit(self.logo, self.logo_rect)
        self.cekvolumebar()
        self.soundbar()

        for button in self.buttons:
            self.buttons[button].update(self.__currentbutton, "positive")
