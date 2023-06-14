from game.components.enemies.enemy import Enemy

class EnemyManager:
	def __init__(self, max_enemies):
		self.enemies = []
		self.max_enemies = max_enemies #aqui

	def update(self):
		self.add_enemy()
		for enemy in self.enemies:
			enemy.update(self.enemies)
	def add_enemy(self):
		if len(self.enemies) < self.max_enemies: #aqui
			enemy = Enemy()
			self.enemies.append(enemy)

	def draw(self, screen):
		for enemy in self.enemies:
			enemy.draw(screen)