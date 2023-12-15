import pygame
import sys
from leaderboard import Leaderboard
from pygame.locals import (
    K_SPACE
)
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, draw_text

from player import Player
from enemy import Enemy


class Game():
    def __init__(self, screen, ADD_ENEMY):
        self.screen = screen
        self.all_sprites = pygame.sprite.Group()
        self.ADD_ENEMY = ADD_ENEMY
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = Player(self.all_sprites, self.bullets)
        self.all_sprites.add(self.player)
        self.shrift = pygame.font.Font(None, 36)
        self.score = 0
        self.state = 'main_menu'
        self.new_game = True
        self.player_name = ''
        self.leaderboard = Leaderboard(self.screen)
    def game(self):
        self.collide = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        if self.collide:
            self.score += 1
        for x in self.collide:
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
        draw_text("Score: " + str(self.score), self.shrift, (200, 200, 200), SCREEN_HEIGHT + 60, SCREEN_WIDTH - 250,
                  self.screen)
        self.enemies.update()
        self.all_sprites.update()
        self.bullets.update()
        for e in self.all_sprites:
            self.screen.blit(e.image, e.rect)
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.kill()
            self.state = 'game_over'
            self.new_game = True
            self.leaderboard.insert_update(self.player_name, self.score)
    def main_menu(self):
            draw_text('Safe Your Soul(SYS)', self.shrift, (200, 200, 200), SCREEN_HEIGHT - 600, SCREEN_WIDTH - 800, self.screen)
            draw_text("Введите имя", self.shrift, (255, 255, 255), 50, 100, self.screen)
            draw_text(self.player_name, self.shrift, (255, 255, 255), 230,  100, self.screen)

            draw_text('Вверх, вниз, влево, вправо - стрелки. Пробел - стрелять', self.shrift, (200, 200, 200), SCREEN_HEIGHT - 550, SCREEN_WIDTH - 600, self.screen)
            draw_text('Таблица рекордов:', self.shrift, (200, 200, 200), SCREEN_HEIGHT - 600, SCREEN_WIDTH - 770, self.screen)
            self.leaderboard.print()
    def game_over(self):
        draw_text('Game Over...', self.shrift, (200, 200, 200), SCREEN_HEIGHT - 300, SCREEN_WIDTH - 600, self.screen)
        draw_text('Нажмите на пробел, чобы выйти в главное меню', self.shrift, (200, 200, 200), SCREEN_HEIGHT - 500, SCREEN_WIDTH - 550, self.screen)
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == self.ADD_ENEMY:
                enemy = Enemy()
                self.all_sprites.add(enemy)
                self.enemies.add(enemy)
            elif event.type == pygame.KEYDOWN and len(self.player_name) >= 2:
                if self.state == 'main_menu':
                    if event.key == pygame.K_SPACE:
                        self.state = 'game'
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    else:
                        if len(self.player_name) < 10 and event.key != pygame.K_SPACE:
                            self.player_name += event.unicode
                elif self.state == 'game_over':
                    if event.key == pygame.K_SPACE:
                        self.state = 'main_menu'
        if self.state == 'main_menu':
            self.main_menu()
        elif self.state == 'game':
            if self.new_game:
                self.all_sprites = pygame.sprite.Group()
                self.enemies = pygame.sprite.Group()
                self.bullets = pygame.sprite.Group()
                self.player = Player(self.all_sprites, self.bullets)
                self.all_sprites.add(self.player)
                self.score = 0
                self.new_game = False
            self.game()
        else:
            self.game_over()



