import pygame

class Projectile:
    def __init__(self, pos, screen, speed, owner):
        ### PLAYER STATS ###
        self.color = (255, 255, 255)
        self.width = 5
        self.height = 3
        self.speed = speed
        self.position = pos
        self.owner = owner
        ### DEBUG MODE ###
        self.debug = False
        self.collision_offset = [10,10]
        self.debug_collision_color = (0, 255, 0)
        self.screen = screen
        self.bulletColor = (200, 100, 200)
        self.projectiles = []


    def Draw(self):
         pygame.draw.circle(self.screen, self.bulletColor, self.position, self.width, self.height )

    def UpdateCollisionArea(self):
        collision_area = [self.position[0] - self.collision_offset[0], self.position[1] - self.collision_offset[1]]
        self.b_box= pygame.Rect(*collision_area, 2* self.collision_offset[0],2* self.collision_offset[1])
        if self.debug:
            pygame.draw.rect(self.screen, self.debug_collision_color, self.b_box, 1)

    def Update(self):
        if self.owner == "player":
            self.position[1] -= self.speed

        elif self.owner == "enemy":
            self.position[1] += self.speed
        self.UpdateCollisionArea()

    def LastBullet(self):
        return self.projectiles[-1]