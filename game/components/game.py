import pygame
import random
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu


from game.components.bullets.bullet_manager import BulletManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()  # aqui
        self.bullet_manager = BulletManager(self.enemy_manager)
        self.score = 0
        self.hight_score = 0
        self.death_count = 0
        self.menu = Menu("Press any key to start...", self.screen)

        self.max_enemy_speed = 5
        self.enemy_speed_increment = 0.2

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.enemy_manager.reset()
        self.score = 0
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.update_enemy_speed()
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        self.draw_max_enemies()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))

        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(
                image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def update_enemy_speed(self):
        enemy_speed = self.max_enemy_speed + self.score * self.enemy_speed_increment
        for enemy in self.enemy_manager.enemies:
            enemy.speed_x = enemy_speed
            enemy.speed_y = enemy_speed
        if (self.score / self.enemy_manager.max_enemies) == 5:
            self.enemy_manager.max_enemies += 1
            if self.enemy_manager.timer_enemy == 500:
                self.enemy_manager.timer_enemy = 500
            else:
                self.enemy_manager.timer_enemy -= 250
            print(self.enemy_manager.max_enemies)
            print(self.enemy_manager.timer_enemy)

    def show_menu(self):
        self.menu.reset_screen_color(self.screen, self.death_count)

        if self.death_count == 0:
            self.menu.draw(self.screen)
        else:
            # self.menu.update_message("Game over. Press any key to restart")
            # self.menu.draw(self.screen)
            if self.score > self.hight_score:
                self.hight_score = self.score

            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("Game Over", True, (255, 0, 0))
            self.create_text(text, 580, 185)

            text = font.render(f"Your Score: {self.score}", True, (255, 255, 255))
            self.create_text(text, 580, 260)

            text = font.render(f"Highest score: {self.hight_score}", True, (255, 255, 255))
            self.create_text(text, 580, 345)

            text = font.render(f"Total Deaths: {self.death_count}", True, (255, 255, 255))
            self.create_text(text, 580, 435)

            icon = pygame.transform.scale(ICON, (80, 120))
            self.screen.blit(
                icon, (540, 20))

        self.menu.update(self)

    def update_score(self):
        self.score += 1

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"SCORE: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_max_enemies(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"ENEMIES: {self.enemy_manager.max_enemies}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (100, 50)
        self.screen.blit(text, text_rect)

    def create_text(self, text, width, height):
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text, text_rect)
