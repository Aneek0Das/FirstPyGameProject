import pygame

from pygame.locals import (
    RLEACCEL,
    KEYDOWN,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    QUIT
)

#move_up_sound = pygame.mixer.Sound("Up-Down.wav")
#move_down_sound = pygame.mixer.Sound("Up-Down.wav")

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height,up_sound, down_sound):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.width = width
        self.height = height
        self.up_sound = up_sound
        self.down_sound = down_sound

    def update(self, pressed_keys):
        print(self.rect)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            self.up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            self.down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.width:
            self.rect.right = self.width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.height:
            self.rect.bottom = self.height

