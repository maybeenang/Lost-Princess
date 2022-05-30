import pygame
from Assets.Tools import *
from Assets.Settings import *
from Assets.Level_set import *
from Assets.layoutMenuPath import *
from Assets.soundPath import *
from Module.ItemPack.Bendera import Bendera
from Module.ItemPack.Block import Block
from Module.ItemPack.Pisang import Pisang
from Module.ItemPack.Hati import Hati
from Module.ItemPack.Obor import Obor
from Module.ItemPack.Tiang import Tiang
from Module.ItemPack.Particle import Particle
from Module.ItemPack.Background import Background
from Module.ItemPack.Lava import Lava
from Module.Entitypack.Player import Player
from Module.Entitypack.Enemy import Enemy
from Module.MenuPack.Pause import *
from Module.MenuPack.Gameover import *

class Level:
    def __init__(self, level, surface, mainmenu, oldmaxlevel):
        self.surface = surface
        self.camera_x = 0
        self.current_x = 0
        self.bgsound = pygame.mixer.Sound(soundPath['ingamebacksound'])
        self.bgsound.play(-1)
        self.newmaxlevel = level['unlock']
        self.oldmaxlevel = oldmaxlevel

        level_layout = read_csv(level['floor'])
        pisang_layout = read_csv(level['pisang'])
        hati_layout = read_csv(level['hati'])
        enemy_layout = read_csv(level['enemy'])
        bendera_layout = read_csv(level['bendera'])
        obor_layout = read_csv(level['obor'])
        tiang_layout = read_csv(level['tiang'])

        self.level_width = len(level_layout[0]) * BLOCKSIZE
        # print(self.level_width)


        self.status = "running"        
        # mainmenu
        self.mainmenu = mainmenu
        self.pause = Pause(self.surface, self.mainmenu, self.setstatus, oldmaxlevel)

        # setup player
        player_layout = read_csv(level['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.Group()
        self.setupplayer(player_layout)


        self.floor = self.setuplevel(level_layout, 'floor')
        self.pisang = self.setuplevel(pisang_layout, 'pisang')
        self.hati = self.setuplevel(hati_layout, 'hati')
        self.bendera = self.setuplevel(bendera_layout, 'bendera')
        self.obor = self.setuplevel(obor_layout, 'obor')
        self.tiang = self.setuplevel(tiang_layout, 'tiang')
        self.enemy = self.setuplevel(enemy_layout, 'enemy')
        self.batasenemy = self.setuplevel(enemy_layout, 'batasenemy')

        self.bg = pygame.sprite.Group()
        self.setupbackground(self.level_width)

        self.lava = pygame.sprite.Group()
        self.setuplava(self.level_width)

        self.particle = pygame.sprite.GroupSingle()
        self.player_ground = False

    def setuplava(self, level_width):
        lava_start = -WIDTH
        lava_width = 192
        lava_full = int((level_width + WIDTH * 2) / lava_width)

        for col in range(lava_full):
            x = col * lava_width + lava_start 
            y = HEIGHT - 40
            lava = Lava(x, y, lava_width)
            self.lava.add(lava)
    
    def setupbackground(self, layout):
        for i in range(-layout, layout * 2, BLOCKSIZE):
            for j in range(0, HEIGHT, BLOCKSIZE):
                if j < 1 * BLOCKSIZE:
                    self.bg.add(Background((i, j), pygame.image.load(LEVEL_IMG['bgtop'])))
                elif j > 15 * BLOCKSIZE:
                    self.bg.add(Background((i, j), pygame.image.load(LEVEL_IMG['bgbot'])))
                else:
                    self.bg.add(Background((i, j), pygame.image.load(LEVEL_IMG['bgmid'])))
    
    def setupplayer(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE

                if col != '-1':
                    if col == '0':
                        player = Player((x, y), BLOCKSIZE, self.surface, self.jump_particleplayer)
                        self.player.add(player)
                    if col == '1':
                        img = slice_img(LEVEL_IMG['batasplayer'])[int(col)]
                        batasplayer = Block((x, y), BLOCKSIZE, img)
                        self.goal.add(batasplayer)
    
    def cek_goal(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.goal, False):
            self.bgsound.stop()
            self.mainmenu(self.newmaxlevel)
    
    def cek_death(self):
        if self.player.sprite.rect.top > HEIGHT:
            self.bgsound.stop()
            self.player.sprite.health_now = 0
            self.mainmenu(self.oldmaxlevel)
        
    def createpause(self):
        self.bgsound.stop()
        self.pause.draw()
        self.pause.input()
    
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
        dumb = pygame.sprite.Group()

        for row_index, row in enumerate(level):
            for col_index, col in enumerate(row):
                x = col_index * BLOCKSIZE
                y = row_index * BLOCKSIZE
                if col != '-1':

                    if type == 'floor':
                        img = slice_img(LEVEL_IMG['floor'])[int(col)]
                        block = Block((x, y), BLOCKSIZE, img)
                        dumb.add(block)
                    
                    if type == 'tiang':
                        tiang = Tiang(x, y, BLOCKSIZE)
                        dumb.add(tiang)
                    
                    if type == 'bendera':
                        if col == '0':
                            block = Bendera(x, y, BLOCKSIZE, "merah")
                        elif col == '1':
                            block = Bendera(x, y, BLOCKSIZE, "biru")
                        dumb.add(block)
                    
                    if type == 'pisang':
                        pisang = Pisang(x, y, BLOCKSIZE)
                        dumb.add(pisang)
                    
                    if type == 'hati':
                        hati = Hati(x, y, BLOCKSIZE)
                        dumb.add(hati)
                    
                    if type == 'obor':
                        obor = Obor(x, y, BLOCKSIZE)
                        dumb.add(obor)
                    
                    if type == 'enemy':
                        if col == '0':
                            enemy = Enemy((x, y), BLOCKSIZE)
                            dumb.add(enemy)
                    
                    if type == 'batasenemy':
                        if col == '1':
                            img = slice_img(LEVEL_IMG['batasenemy'])[int(col)]
                            batasenemy = Block((x, y), BLOCKSIZE, img)
                            dumb.add(batasenemy)
        return dumb

    def enemyreverse(self):
        for enemy in self.enemy.sprites():
            if pygame.sprite.spritecollide(enemy, self.batasenemy, False):
                enemy.reverse()
    
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
        for i in item:
            if player.rect.colliderect(i.rect):
                player.get_health(100)
                i.kill()
    
    def coll_enemy(self):
        collision = pygame.sprite.spritecollide(self.player.sprite, self.enemy, False)

        if collision:
            for enemy in collision:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.sprite.pos.y >= 0:
                    enemy.kill()
                    self.player.sprite.pos.y = -10
                else:
                    self.player.sprite.get_dmg(100)
    
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

            self.bg.draw(self.surface)
            self.bg.update(self.camera_x)

            self.particle.update(self.camera_x)
            self.particle.draw(self.surface)

            self.floor.update(self.camera_x)
            self.floor.draw(self.surface)

            self.tiang.update(self.camera_x)
            self.tiang.draw(self.surface)

            self.bendera.update(self.camera_x)
            self.bendera.draw(self.surface)

            self.pisang.update(self.camera_x)
            self.pisang.draw(self.surface)

            self.hati.update(self.camera_x)
            self.hati.draw(self.surface)

            self.obor.update(self.camera_x)
            self.obor.draw(self.surface)

            self.enemy.update(self.camera_x)
            self.batasenemy.update(self.camera_x)
            self.enemyreverse()
            self.enemy.draw(self.surface)

            self.goal.update(self.camera_x)
            # self.goal.draw(self.surface)

            self.player.update()
            self.player.sprite.health_bar(self.surface)
            self.coll_item(self.player.sprite, self.hati.sprites())
            self.coll_item(self.player.sprite, self.pisang.sprites())
            self.collision_x(self.player.sprite, self.floor.sprites())
            self.set_player_ground()
            self.collision_y(self.player.sprite, self.floor.sprites())
            self.land_particleplayer()
            self.player.draw(self.surface)

            self.lava.update(self.camera_x)
            self.lava.draw(self.surface)

            self.coll_enemy()
            self.camera()
            self.cek_goal()
            self.cek_death()
        elif self.status == "pause":
            self.createpause()
        
        self.input()