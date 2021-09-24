import timeit

import pygame
from Projectile import Projectile
import time


class Enemy:
    def __init__(self, screen, player, tab_enemies):
        self.screen = screen
        self.speed = 50
        self.pos = [250, 50]
        self.state = True
        self.cooldown = 0.25
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
        next_shoot = 1
        print(time.time())
        if next_shoot <= self.cooldown:
            self.projectiles.append(Projectile(self.pos, self.screen, "Enemy"))

            next_shoot -= timeit.timeit("Shoot()", number=1000)
            print("shoot")
