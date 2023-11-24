import random
import sys

import pygame
from pygame.locals import (
    K_SPACE,
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
pygame.time.set_timer(ADD_ENEMY, random.randrange(300, 700))


class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        super(Player, self).__init__()
        self.image = pygame.Surface((20, 20))
        self.col = (100, 100, 100)
        self.rect = self.image.get_rect()
        self.image.fill(self.col)
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


class Game():
    def __init__(self, screen, ADD_ENEMY):
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.ADD_ENEMY = ADD_ENEMY
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(self.all_sprites, self.bullets)
        self.all_sprites.add(self.player)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == ADD_ENEMY:
                enemy = Enemy()
                self.all_sprites.add(enemy)
                self.enemies.add(enemy)
        self.enemies.update()
        self.all_sprites.update()
        self.bullets.update()
        for e in self.all_sprites:
            self.screen.blit(e.image, e.rect)
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.kill()
            pygame.quit()
            sys.exit()


run = True
game = Game(screen, ADD_ENEMY)
while run:
    clock.tick(FPS)
    screen.fill((0, 0, 40))
    game.update()
    pygame.display.flip()
