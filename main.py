import pygame
import random
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from game import Game


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, random.randrange(300, 700))

game = Game(screen, ADD_ENEMY)
while True:
    clock.tick(FPS)
    screen.fill((0, 0, 40))
    game.update()
    pygame.display.flip()
