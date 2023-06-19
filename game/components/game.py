import pygame
import random
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, FREEZE_TYPE, SKULL_TYPE, SHIELD_TYPE, START_SOUND, LOSE_SOUND

from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.bullets.bullet_manager import BulletManager
from game.components.counter import Counter
from game.components.power_ups.power_up_manager import PowerUpManager


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
        self.score = Counter()
        self.hight_score = Counter()
        self.death_count = Counter()
        self.menu = Menu(self.screen)
        self.power_up_manager = PowerUpManager()

        self.max_enemy_speed = 5
        self.enemy_speed_increment = 0.2

    def execute(self):
        self.running = True
        sound = pygame.mixer.Sound(START_SOUND)
        pygame.mixer.Sound.play(sound)
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset(self):
        self.enemy_manager.reset()
        self.score.reset()
        self.player.reset()
        self.bullet_manager.reset()
        self.power_up_manager.reset()

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
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.draw_max_enemies()
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        pygame.display.update()
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up -
                                 pygame.time.get_ticks())/1000)
            if time_to_show >= 0:
                self.menu.draw(self.screen, f"{self.player.power_up_type.capitalize()} is enabled for  {time_to_show}  in seconds", 500, 50, (255,255,255))
            else:
                if self.player.power_up_type == SKULL_TYPE:
                    self.player.speed_y = 10
                    self.player.speed_x = 10
                    self.enemy_manager.enemies = []
                    self.bullet_manager.enemy_bullets = []
                self.power_up_manager.stop_sound()
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()

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
        enemy_speed = self.max_enemy_speed + self.score.count * self.enemy_speed_increment
        for enemy in self.enemy_manager.enemies:
            if self.player.power_up_type == FREEZE_TYPE or self.player.power_up_type == SKULL_TYPE:
                enemy.speed_y = 1
                enemy.speed_x = 1
                for bullet in self.bullet_manager.enemy_bullets:
                    bullet.speed_enemy = 2
            else:
                enemy.speed_x = enemy_speed
                enemy.speed_y = enemy_speed
                for bullet in self.bullet_manager.enemy_bullets:
                    bullet.speed_enemy = bullet.SPEED
        if (self.score.count / self.enemy_manager.max_enemies) == 5:
            self.enemy_manager.max_enemies += 1
            if self.enemy_manager.timer_enemy == 500:
                self.enemy_manager.timer_enemy = 500
            else:
                self.enemy_manager.timer_enemy -= 250

    def show_menu(self):
        self.menu.reset_screen_color(self.screen, self.death_count.count)

        if self.death_count.count == 0:
            self.menu.draw(self.screen, "Press any key to start...")
        else:
            if self.score.count > self.hight_score.count:
                self.hight_score.set_count(self.score.count)

            self.menu.draw(self.screen, "Game Over", 580, 185, (255, 0, 0))

            self.menu.draw(self.screen, f"Your Score: {self.score.count}", 580, 260, (255, 255, 255))

            self.menu.draw(self.screen, f"Highest score: {self.hight_score.count}", 580, 345, (255, 255, 255))

            self.menu.draw(self.screen, f"Total Deaths: {self.death_count.count}", 580, 435, (255, 255, 255))

            icon = pygame.transform.scale(ICON, (80, 120))
            self.screen.blit(icon, (540, 20))

        self.menu.update(self)
        self.player.set_image()

    def draw_max_enemies(self):
        self.menu.draw(self.screen, f"ENEMIES: {self.enemy_manager.max_enemies}", 100, 50, (255, 255, 255))

    def create_text(self, text, width, height):
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text, text_rect)
