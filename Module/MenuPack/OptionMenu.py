from Module.Menu import *
from Module.MenuPack.Button import *

class OptionMenu(Menu):
    def __init__(self, surface, menu, soundstatus):
        super().__init__(surface)

        self.logo = self.font.render("Option", True, "white")
        self.logo_rect = self.logo.get_rect(center=(350, 50))
        self.currentbutton = 0
        self.createmenu = menu

        # sound click
        # self.soundclick = pygame.mixer.Sound(soundPath['click'])
        # self.soundclicked = [
        #     pygame.mixer.Sound(soundPath['positive_click']), 
        #     pygame.mixer.Sound(soundPath['negative_click']),
        #     pygame.mixer.Sound(soundPath['error_click'])
        # ]
        

        self.soundstatus = soundstatus
        self.buttons = {
            'back': Button(self.surface, (350, 120), 'Back', 0),
            'sound': Button(self.surface, (200, 260), 'Sound', 1)
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
        if keys[pygame.K_s] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == len(self.buttons) - 1:
                self.currentbutton = len(self.buttons)-1
            else:
                # self.soundclick.play()
                self.currentbutton += 1
        elif keys[pygame.K_w] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 0:
                self.currentbutton = 0
            else:
                # self.soundclick.play()
                self.currentbutton -= 1
        
        # horizontal input
        if keys[pygame.K_d] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'sound':
                        if self.soundstatus < 1.0:
                            self.soundstatus += 0.2
                        elif self.soundstatus == 1.0:
                            self.soundstatus = 1.0
        elif keys[pygame.K_a] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'sound':
                        if self.soundstatus > 0.0:
                            self.soundstatus -= 0.2
                        elif self.soundstatus == 0:
                            self.soundstatus = 0.0


        if keys[pygame.K_SPACE] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'back':
                        # self.soundclicked[0].play()
                        self.createmenu()
                    elif button == 'sound':
                        pass
                        # self.soundclicked[2].play()
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
        
        # print("{a}, {b}" .format(a=self.currentvolume / self.volumeratio, b=self.currentvolume))

    def soundbar(self):
        self.value = pygame.draw.rect(self.surface, 'green', (350, 250, self.currentvolume / self.volumeratio, 20), border_radius=8)
        self.border = pygame.draw.rect(self.surface, 'black', (350, 250, self.volumelenght, 20), 3, 8)

    def draw(self):
        self.input()
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)
        self.cekvolumebar()
        self.soundbar()

        for button in self.buttons:
            self.buttons[button].update(self.currentbutton, "positive")
