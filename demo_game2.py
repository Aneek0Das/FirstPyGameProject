import pygame
import player
import enemy
import cloud

from pygame.locals import (
    KEYDOWN,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT
)

pygame.mixer.init()

pygame.init()

# -------------------------------

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

running = True

white = (255, 255, 255)
black = (0, 0, 0)
sky_blue = (153, 217, 234)

ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 500)

move_up_sound = pygame.mixer.Sound("Up-Down.ogg")
move_down_sound = pygame.mixer.Sound("Up-Down.ogg")
collision_sound = pygame.mixer.Sound("Collision.ogg")

player1 = player.Player(SCREEN_WIDTH, SCREEN_HEIGHT, move_up_sound, move_down_sound)


enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)

pygame.mixer.music.load("Background.ogg")
pygame.mixer.music.play(loops=-1)



while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:  # When user presses any key from keyboard
            if event.key == K_ESCAPE:  # When it's the escape key
                running = False
        elif event.type == QUIT:  # When user clicks on close button
            running = False
        elif event.type == ADD_ENEMY:
            new_enemy = enemy.Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADD_CLOUD:
            new_cloud = cloud.Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)


    # Creating new surface
    # surf = pygame.Surface((150, 150))
    # surf.fill((0, 0, 0))
    # rect = surf.get_rect()
    pressed_keys = pygame.key.get_pressed()

    #running = False

    player1.update(pressed_keys)
    enemies.update()
    clouds.update()

    screen.fill(sky_blue)

    #screen.blit(player1.surf, player1.rect)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player1, enemies):
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        pygame.time.delay(1000)
        player1.kill()
        running = False

    pygame.display.flip()

    clock.tick(30)

pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()
