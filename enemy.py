import pygame
import random
from pygame.locals import (
    RLEACCEL)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Enemy, self).__init__()
        #self.surf = pygame.Surface((20, 10))
        self.surf = pygame.image.load("torpedo.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.screen_width = width
        self.screen_height = height
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.screen_width + 20, self.screen_width + 100),
                random.randint(0, self.screen_height),
            )
        )
        self.speed = random.randint(5, 10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()