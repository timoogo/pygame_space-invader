import pygame
from Projectile import Projectile

class Player:
    def __init__(self, screen):
        self.speed = 50
        self.pos = [250,400]
        self.screen_x = screen.get_width() 
        self.state = True
        self.cooldown = 0.25
        self.screen = screen
        self.radius = 20
        print(self.screen_x)
    def Draw(self):
        pygame.draw.circle(self.screen, (0, 200,0), self.pos, self.radius)
        
    def OnMoveEvent(self, event):
        if event.key == pygame.K_q:
            self.Move(-1)
            print(event)
        if event.key == pygame.K_d:
            self.Move(1)
            print(event)
        if event.key == pygame.K_s:
            self.Shoot()
    def Move(self, dir):
        self.pos[0] += dir * self.speed
        if self.pos[0] <= 0 + self.radius:
            self.pos[0] = self.radius
        if self.pos[0] >= self.screen_x - self.radius:
            self.pos[0] = self.screen_x - self.radius
        print(self.speed)
        
    def Shoot(self):
        print("shoot")