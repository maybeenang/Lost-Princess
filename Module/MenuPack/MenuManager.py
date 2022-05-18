from Module.Menu import *
from Module.MenuPack.MainMenu import *
from Module.MenuPack.OptionMenu import *

class MenuManager(Menu):
    def __init__(self, surface):
        super().__init__(surface)

        # backsound menu
        self.bg_sound = pygame.mixer.Sound(Menu_path['sound_bg'])
        # self.bg_sound.play(-1)

        self.mainmenu = MainMenu(self.surface, self.createoption, self.createlevelselect)
        
        self.status = 'main'
        self.soundstatus = 'on'
        # self.soundplay()
    
    def createoption(self):
        self.option = OptionMenu(self.surface, self.createmainmenu, self.soundstatus)
        self.status = 'opt'
    
    def createmainmenu(self):
        self.mainmenu = MainMenu(self.surface, self.createoption, self.createlevelselect)
        self.status = 'main'
    
    def createlevelselect(self):
        self.levelselect = LevelMenu(self.surface, self.createmainmenu)
        self.status = 'level'
    
    def soundplay(self):
        if self.soundstatus == 'on':
            self.bg_sound.play(-1)
        else:
            self.bg_sound.stop()
    
    def draw(self):

        self.soundplay()
        
        if self.status == 'main':
            self.mainmenu.draw()
        elif self.status == 'opt':
            self.option.draw()
            self.soundstatus = self.option.soundstatus
        elif self.status == 'level':
            self.levelselect.draw()
        # print(self.status)