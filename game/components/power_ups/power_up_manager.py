import pygame
import random


from game.components.power_ups.shield import Shield
from game.components.power_ups.freeze import Freeze
from game.components.power_ups.skull import Skull
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, FREEZE_TYPE


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(5, 7)
        self.status_sound = False

    def generate_power_up(self):
        available_power_ups = [Shield, Freeze, Skull]
        percent = [49, 49, 2] #[1, 1, 98]
        power_up_class = random.choices(available_power_ups, weights=percent)[0]
        power_up = power_up_class()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                self.play_sound(power_up)
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                if isinstance(power_up, Shield):
                    power_up.activate(game)
                    self.power_ups.remove(power_up)

                elif isinstance(power_up, Freeze):
                    power_up.activate(game)
                    self.power_ups.remove(power_up)

                elif isinstance(power_up, Skull):
                    power_up.activate(game)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)

    def play_sound(self, power_up):
        if self.status_sound:
            self.stop_sound()
            self.status_sound = False
        self.sound = power_up.sound
        self.sound.play()
        self.status_sound = True


    def stop_sound(self):
        self.sound.stop()
                #break
