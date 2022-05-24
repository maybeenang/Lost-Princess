from ..Item import Item

class Pisang(Item):
    def __init__(self, pos, size, img):
        super().__init__(pos, size)
        self.image = img