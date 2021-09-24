import pygame
from Projectile import Projectile


class Player:
    def __init__(self, screen, tab_enemies):
        self.speed = 0.75
        self.screen_x = screen.get_width()
        self.screen_y = screen.get_height()
        self.offset_y = 150
        self.screen = screen
        self.position = [self.screen_x / 2, self.screen_y - self.offset_y]
        self.alive = True
        self.debug = False
        self.cooldown = 0.25
        self.radius = 20
        self.bulletPos = self.position
        self.bulletColor = (255, 255, 255)
        self.debug_death_color = (0, 0, 0)
        self.projectiles: list[Projectile] = []
        self.tab_enemies = tab_enemies
        self.last_fire = 0


    def Draw(self):
        pygame.draw.circle(self.screen, (0, 180, 0), self.position, self.radius)
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(*self.position, self.radius*2, self.radius*2), 1)
        if not self.alive:
            pygame.draw.rect(self.screen, self.debug_death_color, (0, 300, self.screen_x, 600))
        self.Update()
        for s in self.projectiles:
            s.Draw()

    def Update(self):
        self.OnMoveEvent()
        self.OnCollisionEvent()
        self.OnShootEvent()
        for p in self.projectiles:
            p.Move()
            if p.position[1] > 0:
                del p

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

    def Move(self, vec_dir):
        if self.alive:
            self.position[0] += vec_dir * self.speed
            if self.position[0] <= 0 + self.radius:
                self.position[0] = self.radius
            if self.position[0] >= self.screen_x - self.radius:
                self.position[0] = self.screen_x - self.radius
            print(self.speed)

    def Die(self):
        if self.alive and self.debug:
            self.alive = False
            print(self.alive)

    def OnShootEvent(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last_fire >= 200:
                self.last_fire = now
                start_projectile_pos= [*self.position] # unpacking
                self.projectiles.append(Projectile(start_projectile_pos, self.screen, owner="player"))
