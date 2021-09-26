from Player import *
from Enemy import *
import pygame

module_charge = pygame.init()
print(module_charge)

# Variable to keep the main loop game_is_running
game_is_running = True

favicon = "assets/space_invader_logo.png"

screen = pygame.display.set_mode((500, 500))
# fullscreen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Space Invader by timogo")
img = pygame.image.load(favicon).convert()
print(img)
i = 0
tmp_pos = (0, 0)
tab_enemies = []
player = Player(screen, tab_enemies)
enemy = Enemy(screen,player,  tab_enemies)
tab_enemies.append(Enemy(screen, player, tab_enemies))



while game_is_running:
    screen.fill((0, 0, 0))
    i += 1

    for event in pygame.event.get():
       # enemy.Shoot()
        player.Update()
        enemy.Update()

        if event.type == pygame.QUIT:
            game_is_running = False
    for to_draw in [player, enemy]:
        to_draw.Draw()
    # player.Draw()
    # enemy.Draw()
    pygame.display.flip()
