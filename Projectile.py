import pygame

projectiles = []
class Projectile:
    def __init__(self, pos, screen,owner):
        self.color = (255, 255, 255)
        self.width = 2
        self.speed = 15
        self.position = pos
        self.screen = screen
        self.owner = owner
        self.bulletForm = (10, 10, 5,10)
        self.hasShot = False

    def Draw(self):
        if self.hasShot:
                pygame.draw.rect(self.screen, self.color, self.bulletForm)
                print("shoot")

    def WhoShot(self):
        if self.owner == "Player":
            print("from Player")
            self.hasShot = True
        if self.owner == "Enemy":
            print("from enemy")
