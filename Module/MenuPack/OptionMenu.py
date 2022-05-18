from Module.Menu import *
from Module.MenuPack.Button import *

class OptionMenu(Menu):
    def __init__(self, surface, menu, soundstatus):
        super().__init__(surface)

        self.logo = self.font.render("Option", True, "white")
        self.logo_rect = self.logo.get_rect(center=(310, 50))
        self.currentbutton = 0
        self.createmenu = menu
        

        self.buttons = {
            'back': Button(self.surface, (310, 200), 'Back', 0),
            'sound': Button(self.surface, (310, 260), 'Sound Off', 1)
        }
        self.soundstatus = soundstatus

        # time
        self.time = pygame.time.get_ticks()
        self.delay = 200
    
    def input(self):
        keys = pygame.key.get_pressed()
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

        if keys[pygame.K_SPACE] and (pygame.time.get_ticks() > self.time + self.delay):
            self.time = pygame.time.get_ticks()
            for button in self.buttons:
                if self.buttons[button].input(self.currentbutton):
                    if button == 'back':
                        self.createmenu()
                    elif button == 'sound':
                        if self.soundstatus == "off":
                            self.soundstatus = "on"
                            self.buttons['sound'].temp_text = "Sound Off"
                        else:
                            self.soundstatus = "off"
                            self.buttons['sound'].temp_text = "Sound On"
    
    def soundset(self):
        return self.soundstatus      

    def draw(self):
        self.input()
        self.surface.fill('grey')
        self.surface.blit(self.logo, self.logo_rect)

        if self.soundstatus == "off":
            self.buttons['sound'].temp_text = "Sound On"
        else:
            self.buttons['sound'].temp_text = "Sound Off"

        for button in self.buttons:
            self.buttons[button].update(self.currentbutton)
    
