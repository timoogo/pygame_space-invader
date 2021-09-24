import pygame


class Projectile:
    def __init__(self, pos, screen,owner):
        self.color = (255, 255, 255)
        self.width = 2
        self.speed = 1
        self.vel = 1.15
        self.position = []
        self.position.append(pos[0])
        self.position.append(pos[1])

        self.owner = owner
        self.screen = screen
        self.bulletForm = (10, 10, 50,100)
        self.hasShot = False
        self.projectiles = []

    def Draw(self):
        pygame.draw.circle(self.screen, (0, 180, 0), self.position, 10)

    def Move(self):
        if self.owner == "Player":
            self.position[1] -= self.speed
        else:
            self.position[1] += self.speed