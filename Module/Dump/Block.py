from ..Item import Item

class Block(Item):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image.fill('grey')
    
    def update(self, x):
        self.rect.x += x