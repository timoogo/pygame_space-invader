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

    def Draw(self):
        pygame.draw.circle(self.screen, (0, 180, 0), self.position, self.radius)
        if not self.alive:
            pygame.draw.rect(self.screen, self.debug_death_color, (0, 300, self.screen_x, 600))
        self.Update()
        for s in self.projectiles:
            s.Draw()

    def Update(self):
        self.OnMoveEvent()
        self.OnCollisionEvent()

        for p in self.projectiles:
            p.Move()
            if p.position[1] > 0:
                if int(len(self.projectiles) >=2):
                    del (p)


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

    def Move(self, dir):
        if self.alive:
            self.position[0] += dir * self.speed
            if self.position[0] <= 0 + self.radius:
                self.position[0] = self.radius
            if self.position[0] >= self.screen_x - self.radius:
                self.position[0] = self.screen_x - self.radius
            print(self.speed)

    def Die(self):
        if self.alive and self.debug:
            self.alive = False
            print(self.alive)

    def Shoot(self):
        self.projectiles.append(Projectile(self.position, self.screen, self))
