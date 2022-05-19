from Module.Menu import *
from Module.MenuPack.Button import *

class OptionMenu(Menu):
    def __init__(self, surface, menu, soundstatus):
        super().__init__(surface)

        self.logo = self.font.render("Option", True, "white")
        self.logo_rect = self.logo.get_rect(center=(310, 50))
        self.currentbutton = 0
        self.createmenu = menu

        # sound click
        self.soundclick = pygame.mixer.Sound(Menu_path['sound_klik'])
        self.soundclicked = [
            pygame.mixer.Sound(Menu_path['positive_click']), 
            pygame.mixer.Sound(Menu_path['negative_click']),
            pygame.mixer.Sound(Menu_path['error_click'])
        ]
        

        self.soundstatus = soundstatus
        self.buttons = {
            'back': Button(self.surface, (310, 120), 'Back', 0),
            'sound': Button(self.surface, (180, 260), 'Sound', 1)
        }



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
                self.soundclick.play()
                self.currentbutton += 1
        elif keys[pygame.K_w] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 0:
                self.currentbutton = 0
            else:
                self.soundclick.play()
                self.currentbutton -= 1
        
        # horizontal input
        if keys[pygame.K_d] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'sound':
                        if self.soundstatus < 1:
                            self.soundstatus += 0.05
                        else:
                            self.soundstatus = 1.0
        elif keys[pygame.K_a] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'sound':
                        if self.soundstatus > 0:
                            self.soundstatus -= 0.05
                        else:
                            self.soundstatus = 0.0


        if keys[pygame.K_SPACE] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'back':
                        self.soundclicked[1].play()
                        self.createmenu()
                    elif button == 'sound':
                        self.soundclicked[2].play()
                        # self.soundstatus(0.0)   
    def soundbar(self):

        # garis
        pygame.draw.rect(self.surface, 'white', (300, 255, 270, 5), border_radius=6)
        pygame.draw.rect(self.surface, 'black', (300, 255, 270, 5), 1, 6)

        # circle
        pygame.draw.circle(self.surface, 'white', (300 + (self.soundstatus * 250), 255), 10)
        pygame.draw.circle(self.surface, 'black', (300 + (self.soundstatus * 250), 255), 10, 1)

    def draw(self):
        self.input()
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)
        self.soundbar()

        for button in self.buttons:
            self.buttons[button].update(self.currentbutton)
    
