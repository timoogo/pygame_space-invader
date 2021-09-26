import pygame


class Projectile:
    def __init__(self, pos, screen,owner):
        self.color = (255, 255, 255)
        self.width = 5
        self.speed = 5
        self.vel = 1.15
        self.position = pos
        self.owner = owner
        self.screen = screen
        self.bulletColor = (200, 100, 200)
        self.hasShot = False
        self.projectiles = []

    def Draw(self):
        pygame.draw.circle(self.screen, self.bulletColor, self.position, self.width, 2)

    def Move(self):
        if self.owner == "player":
            self.position[1] -= self.speed
        elif self.owner == "enemy":
            self.position[1] += self.speed
