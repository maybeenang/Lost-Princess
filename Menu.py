<<<<<<< HEAD
# import pygame
# from Assets import *

# class Menu:
#     def __init__(self):
#         pass

#     def start(self):
#         pass

#     def options(self):
#         pass

#     def about(self):
#         pass

#     def quit(self):
#         pass

#     def menu_buttons(self):
#         pass

# class InGameMenu(Menu):
#     def __init__(self):
#         super().__init__()

#     def resume(self):
#         pass

#     def main_menu(self):
#         pass

#     def options(self):
#         return super().options()

#     def quit(self):
#         return super().quit()

#     def menu_buttons(self):
#         return super().menu_buttons()

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
=======
import pygame
from Assets.Menu_set import *
from Module.Button import *

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.bg = pygame.image.load(Menu_path['bg'])
        self.logo = pygame.image.load(Menu_path['logo_game'])
        self.logo_rect = self.logo.get_rect(center=(310, 75))
        self.backsound = pygame.mixer.Sound(Menu_path['sound_bg'])
        self.startbuttons = Button(self.surface, (310, 200), "Start")
        self.quit = Button(self.surface, (310, 280), "Quit")
    
    def cek_button(self, pointer):
        return self.startbuttons.input(pointer)
    
    def draw(self, pointer):
        self.backsound.play(-1)
        self.surface.fill('black')
        self.surface.blit(self.logo, self.logo_rect)
        self.startbuttons.hover(pointer)
        self.startbuttons.update()
        self.quit.hover(pointer)
        self.quit.update()
        

        

        
        

>>>>>>> cda6e31 (commit 11 may)
