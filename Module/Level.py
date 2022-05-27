import pygame
from Assets.Tools import *
from Assets.Settings import *
from Assets.Level_set import *
from Assets.layoutMenuPath import *
from Assets.soundPath import *
from Module.ItemPack.Block import Block
from Module.ItemPack.Pisang import Pisang
from Module.ItemPack.Particle import Particle
from Module.Entitypack.Player import Player
from Module.Entitypack.Enemy import Enemy
from Module.MenuPack.Pause import *
from Module.MenuPack.Gameover import *

class Level:
    def __init__(self, level, surface, mainmenu):
        self.surface = surface
        self.camera_x = 0
        self.current_x = 0
        self.bgsound = pygame.mixer.Sound(soundPath['ingamebacksound'])
        self.bgsound.play(-1)

        level_layout = read_csv(level['floor'])
        player_layout = read_csv(level['player'])
        item_layout = read_csv(level['pisang'])
        enemy_layout = read_csv(level['enemy'])
        self.status = "running"        
        # mainmenu
        self.mainmenu = mainmenu
        self.pause = Pause(self.surface, self.mainmenu, self.setstatus)

        self.item = self.setuplevel(item_layout, 'item')
        self.floor = self.setuplevel(level_layout, 'floor')
        self.player = self.setuplevel(player_layout, 'player')
        self.enemy = self.setuplevel(enemy_layout, 'enemy')

        self.particle = pygame.sprite.GroupSingle()
        self.player_ground = False
    
    def createpause(self):
        self.bgsound.stop()
        self.pause.draw()
        self.pause.input()
        # if self.pause.status == 'resume':
        #     self.bgsound.play(-1)
        #     self.status = "running"
        # elif self.pause.status == 'back':
        #     self.bgsound.stop()
        #     self.mainmenu()
    
    def setstatus(self, status):
        if status == "running":
            self.bgsound.play(-1)
        self.status = status
        

    def input(self):
        if self.status == "running":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                self.setstatus("pause")

    def cek_gameover(self):
        if self.player.sprite.health_now <= 0:
            self.status = "gameover"
    
    def setuplevel(self, level, type):
        if type == 'floor' or type == 'item' or type == 'enemy':
            dumb = pygame.sprite.Group()
        elif type == 'player':
            dumb = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(level):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE

                if col != '-1':

                    if type == 'floor':
                        img = slice_img(LEVEL_IMG['floor'])[int(col)]
                        block = Block((x, y), BLOCKSIZE, img)
                        dumb.add(block)
                    
                    if type == 'item':
                        img = slice_img(LEVEL_IMG['pisang'])[int(col)]
                        pisang = Pisang((x, y), BLOCKSIZE, img)
                        dumb.add(pisang)
                    
                    if type == 'enemy':
                        if col == '0':
                            enemy = Enemy((x, y), BLOCKSIZE)
                            dumb.add(enemy)

                    if type == 'player':
                        if col == '0':
                            player = Player((x, y), BLOCKSIZE, self.surface, self.jump_particleplayer)
                            dumb.add(player)
        return dumb
    
    def collision_x(self, entity, block):
        entity.rect.x += entity.pos.x * entity.speed
        for tile in block:
            if tile.rect.colliderect(entity.rect):
                if entity.pos.x > 0:
                    entity.rect.right = tile.rect.left
                    entity.ke_kanan = True
                    self.current_x = entity.rect.right
                elif entity.pos.x < 0:
                    entity.rect.left = tile.rect.right
                    entity.ke_kiri = True
                    self.current_x = entity.rect.left
        
        if entity.ke_kiri and (entity.rect.left < self.current_x or entity.pos.x >= 0):
            entity.ke_kiri = False
        if entity.ke_kanan and (entity.rect.right > self.current_x or entity.pos.x <= 0):
            entity.ke_kanan = False
                    
    def collision_y(self, entity, block):
        entity.cek_gravity()
        for tile in block:
            if tile.rect.colliderect(entity.rect):
                if entity.pos.y > 0:
                    entity.rect.bottom = tile.rect.top
                    entity.pos.y = 0
                    entity.on_ground = True
                    entity.double_jumps = 0
                elif entity.pos.y < 0:
                    entity.rect.top = tile.rect.bottom
                    entity.pos.y = 0
                    entity.on_ceiling = True
        
        if entity.on_ground and entity.pos.y < 0 or entity.pos.y > 1:
            entity.on_ground = False
            if entity.double_jumps >= 2:
                entity.double_jumps = 0
        if entity.on_ceiling and entity.pos.y > 0.1:
            entity.on_ceiling = False
            if entity.double_jumps >= 2:
                entity.double_jumps = 0
    
    def jump_particleplayer(self, pos):

        if self.player.sprite.arah == "kanan":
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)
        self.particle.add(Particle(pos, "jump"))
    
    def set_player_ground(self):
        if self.player.sprite.on_ground:
            self.player_ground = True
        else:
            self.player_ground = False
    
    def land_particleplayer(self):
        if self.player.sprite.on_ground and not self.player_ground and not self.particle.sprites():
            if self.player.sprite.arah == "kanan":
                offset = pygame.math.Vector2(-7, 15)
            else:
                offset = pygame.math.Vector2(-7, 15)
            self.particle.add(Particle(self.player.sprite.rect.midbottom - offset,'land'))
    
    def coll_item(self, player, item):
        for pisang in item:
            if player.rect.colliderect(pisang.rect):
                player.get_health(100)
                pisang.kill()
    
    def coll_enemy(self, player, enemy):

        for enemy in self.enemy:
            if player.rect.colliderect(enemy.rect):
                player.get_dmg(enemy.damage)
                enemy.kill()
    
    def camera(self):
        player = self.player.sprite
        if player.rect.centerx < WIDTH / 4 and player.pos.x < 0:
            self.camera_x = 4
            player.speed = 0
        elif player.rect.centerx > WIDTH - (WIDTH / 2) and player.pos.x > 0:
            self.camera_x = -4
            player.speed = 0
        else:
            player.speed = 4
            self.camera_x = 0

    
    def draw(self):
        if self.status == "running":
            self.particle.update(self.camera_x)
            self.particle.draw(self.surface)
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
            self.set_player_ground()
            self.collision_y(self.player.sprite, self.floor.sprites())
            self.land_particleplayer()
            self.player.draw(self.surface)
        elif self.status == "pause":
            self.createpause()
        
        self.input()