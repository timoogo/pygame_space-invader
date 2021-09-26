import pygame
from Projectile import Projectile


class Enemy:
    def __init__(self, screen, player, tab_enemies):
        self.cooldown_between_shots = 200

        self.last_fire = 0
        self.screen = screen
        self.speed = 50
        self.position = [250, 50]
        self.state = True
        self.bulletColor = (255, 0, 0)
        self.bulletPos = [250, 55]
        self.enemyColor = (255, 15, 0)
        self.radius = 20
        self.player = player
        self.tab_enemies = tab_enemies
        self.projectiles: list[Projectile] = []
        self.tab_enemies = tab_enemies
        self.cooldown_between_shots = 200
        self.last_fire = 0
    def Draw(self):
        pygame.draw.circle(self.screen, self.enemyColor, self.position, self.radius)
        self.Update()
        for p in self.projectiles:
            p.Draw()

    def Update(self):
        self.OnMoveEvent()
        self.OnShootEvent()
        for p in self.projectiles:
            p.Move()
            if p.position[1] > 0:
                del p

    def OnMoveEvent(self):
        if self.position[0] <= self.screen.get_width() / 2:
            self.Move(-1)
        if self.position[0] >= self.screen.get_width() / 2:
            self.Move(1)

    def Move(self, vec_dir):
        if self.state:
            self.position[0] += vec_dir * self.speed
            if self.position[0] <= 0 + self.radius:
                self.position[0] = self.radius
                self.Move(1)
            if self.position[0] >= self.screen.get_width() - self.radius:
                self.position[0] = self.screen.get_width() - self.radius
                self.Move(-1)

    def OnShootEvent(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            now = pygame.time.get_ticks()
            if now - self.last_fire >= self.cooldown_between_shots:
                print(f'{now} is shot')
                self.last_fire = now
                start_projectile_pos = [*self.position]  # unpacking
                self.projectiles.append(Projectile(start_projectile_pos, self.screen, owner="enemy"))
