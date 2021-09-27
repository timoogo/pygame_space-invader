from Player import *
from Enemy import *
from Projectile import *

import pygame

module_charge = pygame.init()
print(module_charge)

# Variable to keep the main loop game_is_running
game_is_running = True

favicon = "./assets/space_invader_logo.png"

screen = pygame.display.set_mode((500, 500))
s = screen
# fullscreen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Space Invader by timogo")
img = pygame.image.load(favicon).convert()


tmp_pos = (0, 0)
tab_enemies = []
player = Player(screen)
enemy = Enemy(screen, player)
p = Projectile(screen, player.position, 5, "player")
colD = ""
# tab_enemies.append(Enemy(screen, player, tab_enemies))
last_check = 0

def Lose(screen):
    font = pygame.font.Font(None, 36)

    text = font.render("You lost, maybe next time ", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])

def WinScreen(screen):
    font = pygame.font.Font(None, 36)
    # If game over is true, draw game over
    text = font.render("You won", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_x = screen.get_width() / 2 - text_rect.width / 2
    text_y = screen.get_height() / 2 - text_rect.height / 2
    screen.blit(text, [text_x, text_y])
clock = pygame.time.Clock()
while game_is_running:
    clock.tick(300 )
    screen.fill((0, 0, 0))

    now = pygame.time.get_ticks()
    if now -last_check >= 300: # check every 300ms
        for p in player.projectiles:
            if p.b_box.colliderect(enemy.b_box):
                enemy.Die()
        for p in enemy.projectiles:
            if p.b_box.colliderect(player.b_box):
                player.Die()
        last_check = pygame.time.get_ticks()


    if not player.alive:
        Lose(screen)

    elif not enemy.alive:
        WinScreen(screen)

    else:
        for event in pygame.event.get():
            player.Update()
            enemy.Update()
            if event.type == pygame.QUIT:
                game_is_running = False
    for to_draw in [player, enemy]:
        to_draw.Draw()
        # player.Draw()
        # enemy.Draw()
    pygame.display.flip()
