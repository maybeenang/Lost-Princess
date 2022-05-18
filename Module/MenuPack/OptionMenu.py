from Module.Menu import *
from Module.MenuPack.Button import *

class OptionMenu(Menu):
    def __init__(self, surface, menu, soundstatus):
        super().__init__(surface)

        self.logo = self.font.render("Option", True, "white")
        self.logo_rect = self.logo.get_rect(center=(310, 50))
        self.currentbutton = 0
        self.createmenu = menu
        

        self.soundstatus = soundstatus
        self.buttons = {
            'back': Button(self.surface, (310, 200), 'Back', 0),
            'sound': Button(self.surface, (310, 260), 'Sound: ' + str(self.soundstatus), 1)
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
                self.currentbutton += 1
        elif keys[pygame.K_w] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            if self.currentbutton == 0:
                self.currentbutton = 0
            else:
                self.currentbutton -= 1
        
        # horizontal input
        if keys[pygame.K_d] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'sound':
                        if self.soundstatus < 1:
                            self.soundstatus += 0.1
                        else:
                            self.soundstatus = 1
        elif keys[pygame.K_a] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'sound':
                        if self.soundstatus > 0:
                            self.soundstatus -= 0.1
                        else:
                            self.soundstatus = 0


        if keys[pygame.K_SPACE] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'back':
                        self.createmenu()
                    elif button == 'sound':
                        pass
                        # self.soundstatus(0.0)     

    def draw(self):
        self.input()
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)

        # update sound button
        self.buttons['sound'].temp_text = 'Sound: ' + str(self.soundstatus)

        for button in self.buttons:
            self.buttons[button].update(self.currentbutton)
    
