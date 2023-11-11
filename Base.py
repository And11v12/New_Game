import pygame
import random
import time
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
pygame.mixer.init()
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
ADD_ENEMY = pygame.USEREVENT + 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('3.png')
        self.image = pygame.transform.scale(self.image, (7, 8))
        #self.standard_image = pygame.transform.scale(self.image, (60, 25))
        #self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()


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
    screen.fill((0, 0, 0))
    pygame.display.flip()