import pygame
import random
import time




class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('')
        self.image = pygame.transform.scale(self.image, ())
        self.standard_image = pygame.image.load('').convert()
        self.standard_image = pygame.transform.scale(self.image, (60, 25))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()



class Game(object):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def __init__(self):
        self.speed_game = 1