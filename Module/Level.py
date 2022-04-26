import pygame
from Module.Dump.Block import Block
from Module.NPC.Player import Player
from Assets.Settings import *

class Level:
    def __init__(self, level, surface) -> None:
        self.surface = surface
        self.camera_x = 0
        self.setuplevel(level)
    
    def setuplevel(self, level):
        self.Block = pygame.sprite.Group()
        self.Player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(level):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE

                if col == '#':
                    self.Block.add(Block((x, y), BLOCKSIZE))
                
                if col == 'P':
                    self.Player.add(Player((x, y), BLOCKSIZE))
    
    def collision_x(self, entity, block):
        entity.rect.x += entity.pos.x * entity.speed
        for tile in block:
            if tile.rect.colliderect(entity.rect):
                pygame.draw.rect(self.surface, (0, 255, 0), tile.rect)
                if entity.pos.x > 0:
                    entity.rect.right = abs(tile.rect.left)
                    entity.pos.x = 0
                elif entity.pos.x < 0:
                    entity.rect.left = abs(tile.rect.right)
                    entity.pos.x = 0
                    
    def collision_y(self, entity, block):
        entity.cek_gravity()
        for tile in block:
            if tile.rect.colliderect(entity.rect):
                pygame.draw.rect(self.surface, (255, 0, 0), tile.rect)
                if entity.pos.y > 0:
                    entity.rect.bottom = tile.rect.top
                    entity.pos.y = 0
                elif entity.pos.y < 0:
                    entity.rect.top = tile.rect.bottom
                    entity.pos.y = 0
    
    def camera(self):
        player = self.Player.sprite
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
        self.Block.update(self.camera_x)
        self.Block.draw(self.surface)
        self.camera()

        self.Player.update()
        self.collision_x(self.Player.sprite, self.Block.sprites())
        self.collision_y(self.Player.sprite, self.Block.sprites())
        self.Player.draw(self.surface)