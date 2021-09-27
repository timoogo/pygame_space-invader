import math

import pygame
from Projectile import Projectile
from Enemy import  Enemy

class Player:
    def __init__(self, screen):
        ### SOME REQUIRED CALC ###
        self.screen_x = screen.get_width()
        self.screen_y = screen.get_height()
        self.offset_y = 150
        ### SCREEN ###
        self.screen = screen
        ### PLAYER STATS
        self.speed = 2
        self.position  = [int(self.screen_x / 2), int(self.screen_y - self.offset_y)]
        self.alive = True
        ### enemy
        self.enemy = Enemy(screen, self)
        #self.enemy_bullet = self.enemy.bulletPos

        ### PLAYER COLORS AND DEBUG COLLISIONS ###
        self.radius = 20
        self.bullet_speed = 2
        self.player_color = (0, 255, 0)
        self.debug = False
        self.debug_death_color = (0, 0, 0)
        self.collision_color = (0, 255, 0)
        self.collision_offset = [22, 22]
        ### PROJECTILES / SHOOT ###
        self.projectiles: list[Projectile] = []
        self.current_bullet = None
        self.cooldown_between_shots = 400
        self.last_fire = 0
        ### DEBUGMODE ###
        self.debug = False
    def Draw(self):
        pygame.draw.circle(self.screen, self.player_color, self.position, self.radius)


        self.Update()
        for p in self.projectiles:
            p.Draw()

    def Update(self):
        self.OnMoveEvent()
        self.UpdateCollisionArea()
        self.OnCollisionEvent()
        self.OnShootEvent()
        for p in self.projectiles:
            p.Update()
            if p.position[1] > 0:
                del p
#        print(self.enemy_bullet)

    def UpdateCollisionArea(self):
        collision_area = [self.position[0] - self.collision_offset[0], self.position[1] - self.collision_offset[1]]
        self.b_box= pygame.Rect(*collision_area, 2* self.collision_offset[0],2* self.collision_offset[1])
        if self.debug:
            pygame.draw.rect(self.screen, self.collision_color, self.b_box, 1)
    def Move(self, vec_dir):
        if self.alive:
            self.position[0] += vec_dir * self.speed
            if self.position[0] <= 0 + self.radius:
                self.position[0] = self.radius
            if self.position[0] >= self.screen_x - self.radius:
                self.position[0] = self.screen_x - self.radius

    def OnMoveEvent(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.Move(-1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.Move(1)

    def OnCollisionEvent(self):
        col = math.sqrt(math.pow(self.position[0] - self.enemy.position[1], 2) + math.pow(self.position[1] - self.enemy.position[1], 2))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_k]:
            self.debug = True
            self.Die()
        if self.debug and keys[pygame.K_p]:
            print(self.alive)
            self.alive = True

    def OnShootEvent(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_fire >= self.cooldown_between_shots:
                self.last_fire = now
                start_projectile_pos = [*self.position]  # unpacking
                current_projectile = self.projectiles.append(Projectile(start_projectile_pos, self.screen, self.bullet_speed, "player"))

    def Die(self):
        if self.alive :
            self.alive = False
