import pygame
from Projectile import Projectile


class Enemy:
    def __init__(self, screen, player, tab_enemies):
        self.screen = screen
        self.speed = 50
        self.pos = [250, 50]
        self.state = True
        self.last = pygame.time.get_ticks()
        self.cd = 62
        self.bulletColor = (255, 0, 0)
        self.bulletPos = [250, 55]
        self.enemyColor = (255, 15, 0)
        self.radius = 20
        self.player = player
        self.projectiles = []
        self.tab_enemies = tab_enemies


    def Draw(self):
        pygame.draw.circle(self.screen, self.bulletColor, self.pos, self.radius)
        pygame.draw.circle(self.screen, self.bulletColor, self.bulletPos, self.radius/5)



    def Move(self, dir):
        self.pos[0] += dir * self.speed
        print(self.speed)

    def Shoot(self):
        now = pygame.time.get_ticks()
        print(now - self.last)
        if now - self.last >= self.cd:
            print("enemy shot2")
            self.last = now
            self.projectiles.append(Projectile(self.pos, self.screen, "Enemy"))
