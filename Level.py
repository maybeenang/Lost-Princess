import pygame
from Assets.Tools import *
from Assets.Settings import *
from Assets.Level_set import *
from Module.Dump.Block import Block
from Module.Dump.Pisang import Pisang
from Module.NPC.Player import Player
from Module.NPC.Enemy import Enemy

class Level:
    def __init__(self, level, surface):
        self.surface = surface
        self.camera_x = 0

        level_layout = read_csv(level['floor'])
        player_layout = read_csv(level['player'])
        item_layout = read_csv(level['item'])
        enemy_layout = read_csv(level['enemy'])

        self.item = self.setuplevel(item_layout, 'item')
        self.floor = self.setuplevel(level_layout, 'floor')
        self.enemy = self.setuplevel(enemy_layout, 'enemy')
    
        self.player = pygame.sprite.GroupSingle()
        self.setupplayer(player_layout)


    def setupplayer(self, layout):
        player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE
                if col != '-1':
                    img = slice_img(LEVEL_1_IMG['player'])[int(col)]
                    player = Player((x, y), BLOCKSIZE, img)
                    player.rect.centerx = x
                    self.player.add(player)
                

    
    def setuplevel(self, level, type):
        if type == 'floor' or type == 'item' or type == 'enemy':
            dumb = pygame.sprite.Group()

        for row_index, row in enumerate(level):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE

                if col != '-1':

                    if type == 'floor':
                        img = slice_img(LEVEL_1_IMG['floor'])[int(col)]
                        block = Block((x, y), BLOCKSIZE, img)
                        dumb.add(block)
                    
                    if type == 'item':
                        img = slice_img(LEVEL_1_IMG['item'])[int(col)]
                        pisang = Pisang((x, y), BLOCKSIZE, img)
                        dumb.add(pisang)
                    
                    if type == 'enemy':
                        img = slice_img(LEVEL_1_IMG['enemy'])[int(col)]
                        enemy = Enemy((x, y), BLOCKSIZE, img)
                        dumb.add(enemy)
        return dumb
    
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

    def collision_x(self, entity, block):
        entity.rect.x += entity.pos.x * entity.speed

        for tile in block:
            if tile.rect.colliderect(entity.rect):
                if entity.pos.x < 0:
                    entity.rect.left = tile.rect.right
                elif entity.pos.x > 0:
                    entity.rect.right = tile.rect.left
                    
    def collision_y(self, entity, block):
        entity.cek_gravity()
        for tile in block:
            if tile.rect.colliderect(entity.rect):
                if entity.pos.y > 0:
                    entity.rect.bottom = tile.rect.top
                    entity.pos.y = 0
                    entity.on_floor = True
                elif entity.pos.y < 0:
                    entity.rect.top = tile.rect.bottom
                    entity.pos.y = 0
        
        if entity.on_floor and entity.pos.y != 0:
            entity.on_floor = False
    
    def coll_item(self, player, item):

        for pisang in item:
            if player.rect.colliderect(pisang.rect):
                pisang.kill()
                player.get_health(100)
    
    def coll_enemy(self, player, enemy):

        for enemy in self.enemy:
            if player.rect.colliderect(enemy.rect):
                enemy.kill()
                player.get_dmg(enemy.damage)
    

    
    def draw(self):
        self.floor.update(self.camera_x)
        self.floor.draw(self.surface)
        self.item.update(self.camera_x)
        self.item.draw(self.surface)
        self.camera()

        self.enemy.draw(self.surface)
        self.enemy.update(self.camera_x)

        self.player.sprite.health_bar(self.surface)
        self.player.update()
        self.coll_item(self.player.sprite, self.item.sprites())
        self.coll_enemy(self.player.sprite, self.enemy.sprites())
        self.collision_x(self.player.sprite, self.floor.sprites())
        self.collision_y(self.player.sprite, self.floor.sprites())
        self.player.draw(self.surface)