import pygame
from Assets.Tools import importanimation
from Assets.Level_set import LEVEL_IMG
from Module.Entity import Entity

class Player(Entity):
#     player
    def __init__(self, pos, size, surface, jump_particle):
        super().__init__(1000, 10, 4, pos, size)

        self.surface = surface

        # player image
        self.importimage()
        self.index = 0
        self.indexspeed = 0.5
        self.image = self.animation["idle"][self.index]

        # particle image
        self.importparticle()
        self.particle_index = 0
        self.particle_indexspeed = 0.5

        self.jump_particle = jump_particle
        # self.particle_image = self.particle["run"][self.particle_index]


        self.health_now = 200
        self.max_health_bar = 400 
        self.health_ratio = self.health / self.max_health_bar
        self.gravity = 0.9
        self.jump_speed = -10

        # player status
        self.status = "idle"
        self.arah = 'kanan'
        self.on_ground = False
        self.on_ceiling = False
        self.ke_kanan = False
        self.ke_kiri = False
        self.double_jumps = 0

        # time 
        self.time = pygame.time.get_ticks()
        self.delay = 200

    # import animasi particle
    def importparticle(self):
        self.particlerun = importanimation(LEVEL_IMG['particlerun'])
        # for particle in self.particle:
        #     fullpath = particlepath + particle
        #     self.particle[particle] = importanimation(fullpath)
    
    def animasiparticle(self):
        if self.status == "run" and self.on_ground:
            self.particle_index += self.particle_indexspeed
            if self.particle_index >= len(self.particlerun):
                self.particle_index = 0

            particle = self.particlerun[int(self.particle_index)]

            if self.arah == 'kanan':
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.surface.blit(particle, pos)
            elif self.arah == 'kiri':
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                flip = pygame.transform.flip(particle, True, False)
                self.surface.blit(flip, pos)
            

    
    # import animasi perframe ke sebuah list
    def importimage(self):
        playerpath = LEVEL_IMG['player']
        self.animation = {
            "idle": [],
            "run": [],
            "jump": [],
            "fall": []
        }
        for animation in self.animation:
            fullpath = playerpath + animation
            self.animation[animation] = importanimation(fullpath) 
    
    def animate(self):
        self.index += self.indexspeed
        if self.index >= len(self.animation[self.status]):
            self.index = 0
        self.image = self.animation[self.status][int(self.index)]

        if self.arah == 'kiri':
            self.image = pygame.transform.flip(self.image, True, False)
        elif self.arah == 'kanan':
            self.image = pygame.transform.flip(self.image, False, False)

        if self.on_ground and self.ke_kanan:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.ke_kiri:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.ke_kanan:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.ke_kiri:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop) 
    
    def set_status(self):
        if self.pos.y < 0:
            self.status = "jump"
        elif self.pos.y > 1:
            self.status = "fall"
        else:
            if self.pos.x != 0:
                self.status = "run"
            else:
                self.status = "idle"


    
    def get_health(self, health):
        if self.health_now < self.health:
            self.health_now += health
        elif self.health_now > self.health:
            self.health_now = self.health
    
    def get_dmg(self, dmg):
        if self.health_now > 0:
            self.health_now -= dmg
        elif self.health_now <= 0:
            self.health_now = 0
    
    def health_bar(self, screen):

        pygame.draw.rect(screen, (255, 0, 0), (5, 5, self.health_now / self.health_ratio, 25))
        pygame.draw.rect(screen, (0, 255, 0), (5, 5, self.max_health_bar, 25), 1)

    
    def get_input(self):
        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_a]:
            self.move(-1)
            self.arah = 'kiri'
        elif self.keys[pygame.K_d]:
            self.move(1)
            self.arah = 'kanan'
        else:
            self.move(0)
        
        if self.keys[pygame.K_w] and self.on_ground:
            if pygame.time.get_ticks() - self.time > self.delay:
                self.time = pygame.time.get_ticks()
                if self.double_jumps == 0:
                    self.double_jumps = 1
                    self.jump_particle(self.rect.midbottom)
                    self.jump()
        elif self.keys[pygame.K_w] and self.double_jumps == 1:
            if pygame.time.get_ticks() - self.time > self.delay:
                self.time = pygame.time.get_ticks()
                self.jump_particle(self.rect.midbottom)
                self.jump()
                self.double_jumps = 2
    
    def move(self, x):
        self.pos.x = x
        self.rect.x += self.pos.x * self.speed

    def jump(self):
        self.pos.y = self.jump_speed
    
    def cek_gravity(self):
        self.pos.y += self.gravity
        self.rect.y += self.pos.y


    def update(self):
        self.get_input()
        self.set_status()
        self.animate()
        self.animasiparticle()
        # print(self.double_jump)