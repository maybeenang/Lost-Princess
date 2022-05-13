from Module.Menu import *
from Assets.Menu_set import *

class Gameover(Menu):
    def __init__(self, surface):
        super().__init__(surface)
        self.text = "Game Over"
        self.textrender = self.font.render(self.text, True, (255, 255, 255))
        self.textrect = self.textrender.get_rect(center=(310, 75))
    
    def draw(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.textrender, self.textrect)
        pass