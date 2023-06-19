import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SKULL_TYPE, SKULL, SPACESHIP_SKULL, SKULL_SOUND


class Skull(PowerUp):
    def __init__(self):
        super().__init__(SKULL, SKULL_TYPE, SKULL_SOUND)

    def activate(self, game):
        game.player.power_up_type = SKULL_TYPE
        game.player.set_image((64, 75), SPACESHIP_SKULL)
        game.player.speed_y = 20
        game.player.speed_x = 20
        for bullet in game.bullet_manager.bullets:
            bullet.speed_player = 100
