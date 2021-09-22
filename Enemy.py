
import pygame
class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.speed = 50
        self.pos = [250,50]
        self.state = True
        self.cooldown = 0.25

        self.radius = 20
        
    def Draw(self):
        pygame.draw.circle(self.screen, (250, 0,0), self.pos, self.radius)
    def Move(self, dir):
        self.pos[0] += dir * self.speed
        print(self.speed)