import pygame.time
import random
from game.components.enemies.enemy import Enemy

class EnemyManager:
	def __init__(self):
		self.enemies = []
		self.max_enemies = 1 #aqui

		self.enemy_spawn_timer = pygame.time.get_ticks()
		self.timer_enemy = 2500

	def update(self, game):
		self.add_enemy()

		for enemy in self.enemies:
			enemy.update(self.enemies, game)


	def add_enemy(self):
		current_time = pygame.time.get_ticks()
		if len(self.enemies) < self.max_enemies and current_time - self.enemy_spawn_timer >= random.randint(250, self.timer_enemy):
			enemy = Enemy()
			self.enemies.append(enemy)
			self.enemy_spawn_timer = current_time

	def draw(self, screen):
		for enemy in self.enemies:
			enemy.draw(screen)

	def reset(self):
		self.enemies = []