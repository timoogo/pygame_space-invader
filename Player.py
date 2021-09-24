import pygame
from Projectile import Projectile
color = (255, 0, 0)


class Player:
    def __init__(self, screen, tab_enemies):
        self.speed = 0.75
        self.screen_x = screen.get_width()
        self.screen_y = screen.get_height()
        self.offset_y = 150
        self.screen = screen
        self.pos = [self.screen_x / 2, self.screen_y - self.offset_y]
        self.alive = True
        self.debug = True
        self.cooldown = 0.25
        self.radius = 20
        self.bulletPos = self.pos
        self.bulletColor = (255, 0, 0)
        self.projectiles = []
        self.tab_enemies = tab_enemies

    def Draw(self):
        pygame.draw.circle(self.screen, (0, 180, 0), self.pos, self.radius)
        if not self.alive:
            pygame.draw.rect(self.screen, color, (0, 300, self.screen_x, 600))
        else:
            self.Update()
            for s in self.projectiles:
                s.Draw()

    def Update(self):
        self.OnMoveEvent()
        for s in self.projectiles:
            s.Move()

    def OnMoveEvent(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.Move(-1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.Move(1)

    def OnCollisionEvent(self, event):
        if event.key == pygame.K_k:
            self.Die()
        if not self.alive and event.key == pygame.K_p:
            self.alive = True

    def Move(self, dir):
        if self.alive:
            self.pos[0] += dir * self.speed
            if self.pos[0] <= 0 + self.radius:
                self.pos[0] = self.radius
            if self.pos[0] >= self.screen_x - self.radius:
                self.pos[0] = self.screen_x - self.radius
            print(self.speed)

    def Die(self):
        if self.alive and self.debug:
            self.alive = False
            print(self.alive)

    def Shoot(self):
        self.projectiles.append(Projectile(self.pos, self.screen, "Player"))

