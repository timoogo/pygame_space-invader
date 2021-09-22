import pygame
from Player import Player 
from Enemy import Enemy
from Projectile import Projectile
from time import sleep
module_charge = pygame.init()
print (module_charge)

# Variable to keep the main loop game_is_running
game_is_running = True

favicon = "assets/space_invader_logo.png"

screen = pygame.display.set_mode((500,500))
#fullscreen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption(favicon)
img = pygame.image.load(favicon).convert()
print(img)
i = 0
player = Player(screen)
enemy = Enemy(screen)
projectile = Projectile(screen)

while game_is_running:
      screen.fill((0,0,0))
      i += 1
      for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                  player.OnMoveEvent(event)
            if event.type == pygame.QUIT:
                game_is_running = False

      player.Draw()
      enemy.Draw()
      pygame.display.flip()