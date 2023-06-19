import pygame
from game.utils.constants import SHIELD_TYPE, SKULL_TYPE, LOSE_SOUND, ENEMY_DEATH_SOUND


class BulletManager:
    def __init__(self, enemy_manager):
        self.bullets = []
        self.enemy_bullets = []
        self.max_enemy = enemy_manager.max_enemies

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy":
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE and game.player.power_up_type != SKULL_TYPE:
                    sound = pygame.mixer.Sound(LOSE_SOUND)
                    pygame.mixer.Sound.play(sound)
                    game.death_count.update()
                    pygame.time.delay(2000)
                    game.playing = False
                break

        for bullet in self.bullets:
            bullet.update(self.bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == "player":
                    game.enemy_manager.enemies.remove(enemy)
                    sound = pygame.mixer.Sound(ENEMY_DEATH_SOUND)
                    pygame.mixer.Sound.play(sound)
                    self.bullets.remove(bullet)
                    game.score.update()
                    break

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == "enemy":
                self.enemy_bullets.append(bullet)

        elif bullet.owner == "player":
            self.bullets.append(bullet)

    def reset(self):
        self.enemy_bullets = []
