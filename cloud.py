import pygame
import random
from pygame.locals import (
    RLEACCEL)

class Cloud(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("clouds.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.screen_width = width
        self.screen_height = height
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.screen_width + 20, self.screen_width + 100),
                random.randint(0, self.screen_height),
            )
        )
        #self.speed = random.randint(1, 1)

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()