import pygame
from Projectile import Projectile


class Player:
    def __init__(self, screen, tab_enemies):
        ### SOME REQUIRED CALC ###
        self.screen_x = screen.get_width()
        self.screen_y = screen.get_height()
        self.offset_y = 150
        ### SCREEN ###
        self.screen = screen
        ### PLAYER STATS
        self.speed = 0.75
        self.position = [int(self.screen_x / 2), int(self.screen_y - self.offset_y)]
        self.alive = True


        self.debug = False
        ### PLAYER COLORS AND DEBUG COLLISIONS###
        self.radius = 20
        self.player_color = (0, 255, 0)
        self.debug_collision_color = (255, 0, 0)
        self.debug_death_color = (0, 0, 0)
        self.collision_offset = [22, 22]
        self.debug_collision_offset = 45
        ### PROJECTILES / SHOOT ###
        self.projectiles: list[Projectile] = []
        self.tab_enemies = tab_enemies
        self.cooldown_between_shots = 200
        self.last_fire = 0

    def Draw(self):
        pygame.draw.circle(self.screen, self.player_color, self.position, self.radius)
        if not self.alive:
            pygame.draw.rect(self.screen, self.debug_death_color, (0, 300, self.screen_x, 600))

        self.Update()
        for p in self.projectiles:
            p.Draw()

    def Update(self):
        self.OnMoveEvent()
        self.CollisionArea()
        self.OnCollisionEvent()
        self.OnShootEvent()
        for p in self.projectiles:
            p.Move()
            if p.position[1] > 0:
                del p

    def CollisionArea(self):
        debug_collision_area = [self.position[0] - self.collision_offset[0], self.position[1] - self.collision_offset[1]]
        pygame.draw.rect(self.screen, self.debug_collision_color, pygame.Rect(*debug_collision_area, self.debug_collision_offset, self.debug_collision_offset), 1)

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
                self.projectiles.append(Projectile(start_projectile_pos, self.screen, owner="player"))

    def Die(self):
        if self.alive and self.debug:
            self.alive = False
            print(self.alive)
