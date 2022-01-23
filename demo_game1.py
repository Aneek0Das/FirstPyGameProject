import pygame

from pygame.locals import (
    KEYDOWN,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT
)

pygame.init()

# -------------------------------

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

white = (255, 255, 255)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:  # When user presses any key from keyboard
            if event.key == K_ESCAPE:  # When it's the escape key
                running = False
        elif event.type == QUIT:  # When user clicks on close button
            running = False

    screen.fill(white)

    # Creating new surface
    surf = pygame.Surface((150, 150))
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    screen.blit(surf, ((SCREEN_WIDTH - surf.get_width()) / 2, (SCREEN_HEIGHT - surf.get_height()) / 2))


    pygame.display.flip()

pygame.quit()
