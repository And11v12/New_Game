import pygame
import random
import time
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_UP
)
pygame.mixer.init()
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
ADD_ENEMY = pygame.USEREVENT + 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((20, 20))
        self.col = (100, 100, 100)
        self.rect = self.image.get_rect()
        self.surface.fill(self.col)
    def update(self)
        keyUpdate = pygame.key.get_pressed()
        if keyUpdate == K_DOWN:
            self.rect.move_ip(0, 5)
        if keyUpdate == K_UP:
            self.rect.move_ip(0, -5)
        if keyUpdate == K_LEFT:
            self.rect.move_ip(0, 5)
        if keyUpdate == K_RIGHT:
            self.rect.move_ip(0, -5)
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = SCREEN_HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0


class Game():
    def __init__(self, screen):
        self.screen = screen
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

game = Game(screen)
run = True
while run:
    clock.tick(FPS)
    game.update()
    screen.fill((0, 0, 40))
    pygame.display.flip()