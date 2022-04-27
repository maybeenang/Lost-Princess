import pygame
from Assets.Tools import *
from Assets.Settings import *
from Assets.Level_set import *
from Module.Dump.Block import Block
from Module.NPC.Player import Player

class Level:
    def __init__(self, level, surface):
        self.surface = surface
        self.camera_x = 0


        level_layout = read_csv(level['floor'])
        player_layout = read_csv(level['player'])
        self.floor = self.setuplevel(level_layout, 'floor')
        self.player = self.setuplevel(player_layout, 'player')
    
    def setuplevel(self, level, type):
        if type == 'floor':
            dumb = pygame.sprite.Group()
        elif type == 'player':
            dumb = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(level):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE

                if col != '-1':

                    if type == 'floor':
                        img = slice_img(LEVEL_1_IMG['floor'])[int(col)]
                        block = Block((x, y), BLOCKSIZE, img)
                        dumb.add(block)

                    if type == 'player':
                        img = slice_img(LEVEL_1_IMG['player'])[int(col)]
                        player = Player((x, y), BLOCKSIZE, img)
                        dumb.add(player)
        return dumb
                
                # if col == 'P':
                #     self.Player.add(Player((x, y), BLOCKSIZE))
    
    def collision_x(self, entity, block):
        entity.rect.x += entity.pos.x * entity.speed
        for tile in block:
            if tile.rect.colliderect(entity.rect):
                # pygame.draw.rect(self.surface, (0, 255, 0), tile.rect)
                if entity.pos.x > 0:
                    entity.rect.right = tile.rect.left
                    entity.pos.x = 0
                elif entity.pos.x < 0:
                    entity.rect.left = tile.rect.right
                    entity.pos.x = 0
                    
    def collision_y(self, entity, block):
        entity.cek_gravity()
        for tile in block:
            if tile.rect.colliderect(entity.rect):
                # pygame.draw.rect(self.surface, (255, 0, 0), tile.rect)
                if entity.pos.y > 0:
                    entity.rect.bottom = tile.rect.top
                    entity.pos.y = 0
                elif entity.pos.y < 0:
                    entity.rect.top = tile.rect.bottom
                    entity.pos.y = 0
    
    def camera(self):
        player = self.player.sprite
        if player.rect.centerx < WIDTH / 4 and player.pos.x < 0:
            self.camera_x = 4
            player.speed = 0
        elif player.rect.centerx > WIDTH - (WIDTH / 4) and player.pos.x > 0:
            self.camera_x = -4
            player.speed = 0
        else:
            player.speed = 4
            self.camera_x = 0

    
    def draw(self):
        self.floor.update(self.camera_x)
        self.floor.draw(self.surface)
        self.camera()

        self.player.update()
        self.collision_x(self.player.sprite, self.floor.sprites())
        self.collision_y(self.player.sprite, self.floor.sprites())
        self.player.draw(self.surface)