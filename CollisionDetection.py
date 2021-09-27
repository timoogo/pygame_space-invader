import pygame
import Projectile
class CollisionDetection:
    def __init__(self,screen, player, enemy, bullets):
        self.screen = screen,
        self.player = player
        self.enemy = enemy
        self.bullets = bullets
        bullets = list[Projectile]

    def Update(self):
        if self.enemy.has_shot:
            print("kill")