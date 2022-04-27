from ..Item import Item

class Block(Item):
    def __init__(self, pos, size, img):
        super().__init__(pos, size)
        self.image = img
    
    def update(self, x):
        self.rect.x += x