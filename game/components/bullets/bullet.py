import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT, SKULL_TYPE


class Bullet(Sprite):
    X_POS = 80
    Y_POS = 310
    SPEED = 20
    SPEED_PLAYER = 20
    def __init__(self, spaceship):
        BULLET_SIZE = None  # Valor predeterminado
        if spaceship.type == "player":
            if spaceship.power_up_type == SKULL_TYPE:
                BULLET_SIZE = pygame.transform.scale(BULLET, (20, 40))
            else:
                BULLET_SIZE = pygame.transform.scale(BULLET, (10, 20))
        BULLET_SIZE_ENEMY = pygame.transform.scale(BULLET_ENEMY, (9, 32))
        BULLETS = {"player": BULLET_SIZE, "enemy": BULLET_SIZE_ENEMY}
        self.image = BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type
        if spaceship.type == "player":
            if spaceship.power_up_type == SKULL_TYPE:
                self.speed_player = 40
            else:
                self.speed_player = self.SPEED_PLAYER
        self.speed_enemy = self.SPEED

    def events(self):
        pass

    def update(self, bullets):
            if self.owner == "player":
                self.rect.y -= self.speed_player
            else:
                self.rect.y += self.speed_enemy

            if self.rect.y >= SCREEN_HEIGHT or self.rect.y < 0:     
                bullets.remove(self)



    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
