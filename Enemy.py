
import pygame
from Projectile import Projectile
class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.speed = 50
        self.pos = [250,50]
        self.state = True
        self.cooldown = 0.25
        self.projectile_instance = Projectile(screen, self.pos, self)
        self.bulletColor = (255, 0, 0)
        self.bulletPos = [250, 55]
        self.enemyColor = (255, 15, 0)
        self.radius = 20
        
    def Draw(self):
        pygame.draw.circle(self.screen, (self.bulletColor), self.pos, self.radius)
        pygame.draw.circle(self.screen, (self.bulletColor), self.bulletPos, self.radius/5)

    def Move(self, dir):
        self.pos[0] += dir * self.speed
        print(self.speed)
    def Shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_e]:
            self.Draw()
            self.projectile_instance.owner = "Enemy"
            self.projectile_instance.WhoShot()

