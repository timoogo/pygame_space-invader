import pygame


class Projectile:
    def __init__(self, pos, screen,owner):
        self.color = (255, 255, 255)
        self.width = 2
        self.speed = 5
        self.vel = 1.15
        self.position = pos
        self.owner = owner
        self.screen = screen
        self.bulletColor = (200, 100, 200)
        self.hasShot = False
        self.projectiles = []

    def Draw(self):
        pygame.draw.circle(self.screen, self.bulletColor, self.position, 10)

    def Move(self):
        if self.owner == "player":
            self.position[1] -= self.speed
        else:
            self.position[1]  += self.speed
