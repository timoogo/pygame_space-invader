import pygame
from Projectile import Projectile
from time import sleep
color = (0, 0, 0)

class Player:
    def __init__(self, screen):
        self.speed = 0.75
        self.pos = [250, 400]
        self.projectile_instance = Projectile(self.pos, screen, self)
        self.screen_x = screen.get_width()
        self.alive = True
        self.debug = True
        self.cooldown = 0.25
        self.screen = screen
        self.radius = 20
        self.bulletPos = [250, 395]
        self.bulletColor = (255, 0, 0)


    def Draw(self):
        pygame.draw.circle(self.screen, (0, 180, 0), self.pos, self.radius)
        if not self.alive:
            pygame.draw.rect(self.screen, color, (0, 300, self.screen_x, 600))
        else:
            self.Update()
    def Update(self):
        self.OnMoveEvent()
    def OnMoveEvent(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or keys[pygame.K_LEFT]:
            self.Move(-1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.Move(1)
        if keys[pygame.K_SPACE]:
            self.Shoot()
            print(sleep(2))


    def OnCollisionEvent(self, event):
        if event.key == pygame.K_k:
            self.Die()
        if not self.alive and event.key == pygame.K_p:
            self.alive = True

    def Move(self, dir):
        self.pos[0] += dir * self.speed
        if self.pos[0] <= 0 + self.radius:
            self.pos[0] = self.radius
        if self.pos[0] >= self.screen_x - self.radius:
            self.pos[0] = self.screen_x - self.radius
        print(self.speed)

    def Shoot(self):
        self.projectile_instance.owner = "Player"
        self.projectile_instance.WhoShot()
        self.projectile_instance.Draw()

    def Die(self):
        if self.alive and self.debug:
            self.alive = False
            print(self.alive)
