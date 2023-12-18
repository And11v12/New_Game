import pygame
import random

from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.col = (200, 200, 200)
        self.image = pygame.image.load('213.png')
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        self.speed = 4

    def update(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.kill()
