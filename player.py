import pygame
from pygame.locals import (
    K_SPACE,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_UP
)
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        super(Player, self).__init__()
        self.image = pygame.image.load('3.png')
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.bullets = bullets
        self.all_sprites = all_sprites
        self.get_ticks = pygame.time.get_ticks()
        self.shot_speed = 250

    def update(self):
        keyUpdate = pygame.key.get_pressed()
        if keyUpdate[K_DOWN]:
            self.rect.move_ip(0, 5)
        if keyUpdate[K_UP]:
            self.rect.move_ip(0, -5)
        if keyUpdate[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if keyUpdate[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if keyUpdate[K_SPACE]:
            self.shoot()
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        self.now = pygame.time.get_ticks()
        if self.now - self.get_ticks > self.shot_speed:
            self.get_ticks = self.now
            bullet = Bullet(self.rect.x, self.rect.y)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        super(Bullet, self).__init__()
        self.image = pygame.Surface((10, 10))
        self.col = (120, 20, 20)
        self.image.fill(self.col)
        self.rect = self.image.get_rect()
        self.speed = 4
        self.rect.x = posX
        self.rect.y = posY

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()