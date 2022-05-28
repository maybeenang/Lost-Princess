from Module.Game import *
import os
# os.environ["SDL_VIDEODRIVER"] = "dummy"

# menjalankan games
if __name__ == '__main__':
    pygame.init()
    game = Game()

# import pygame

# pygame.init()
# window=pygame.display.set_mode((500, 500))

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()
    
#     window.fill((0,0,0))
#     pygame.display.update()