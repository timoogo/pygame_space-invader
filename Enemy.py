import pygame
import random
from Projectile import Projectile


class Enemy:
    def __init__(self, screen, player):
        self.cooldown_between_shots = 400
        self.last_fire = 0
        self.screen = screen
        self.speed = 0.5
        self.bullet_speed = 0.8
        self.position = [250, 50]
        self.alive = True
        self.bulletColor = (255, 0, 0)
        self.enemyColor = (255, 15, 0)
        self.radius = 20
        self.player = player
        self.projectiles: list[Projectile] = []
        self.last_fire = 0
        ### collision
        self.collision_color = (255, 0, 0)
        self.collision_offset = [22, 22]

        ### DEBUGMODE ###
        self.debug = False
    def Draw(self):
        pygame.draw.circle(self.screen, self.enemyColor, self.position, self.radius)
        self.Update()
        for p in self.projectiles:
            p.Draw()

    def Update(self):
        self.OnMoveEvent()
        self.OnShootEvent()
        self.CollisionArea()
        for p in self.projectiles:
            p.Update()
            if p.position[1] > 0:
                del p

    def OnMoveEvent(self):
        if self.alive:
            if self.position[0] < self.radius:
                self.position[1]+=50
                self.speed = -self.speed
            elif self.position[0] >= self.screen.get_width() - self.radius:
                self.position[1] += 50
                self.speed = -self.speed
            self.position[0] += self.speed



    def OnShootEvent(self):
        now = pygame.time.get_ticks()
        if now - self.last_fire >= self.cooldown_between_shots:
            self.last_fire = now
            if random.randint(1, 100) <= 15: # shoots 15% of the time

                    start_projectile_pos = [*self.position]  # unpacking
                    self.projectiles.append(Projectile(start_projectile_pos, self.screen, self.bullet_speed, "enemy"))
    def CollisionArea(self):
        collision_area = [self.position[0] - self.collision_offset[0], self.position[1] - self.collision_offset[1]]
        self.b_box= pygame.Rect(*collision_area, 2* self.collision_offset[0],2* self.collision_offset[1])
        if self.debug:
            pygame.draw.rect(self.screen, self.collision_color, self.b_box, 1)

    def Die(self):
        if self.alive:
            self.alive = False

