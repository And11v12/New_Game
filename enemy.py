import pygame
import random

from settings import SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((20, 20))
        self.col = (200, 200, 200)
        self.image.fill(self.col)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        self.speed = 4

    def update(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.kill()
