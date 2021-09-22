import pygame
class Projectile:
   def __init__(self,position, screen):
       self.width  = 2
       self.height = 4
       self.speed  = 15
       self.position = position
       self.screen = screen
       