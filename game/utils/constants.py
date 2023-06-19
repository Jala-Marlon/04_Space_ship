import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUND_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
#MUSIC
SHOOT_SOUND = os.path.join(IMG_DIR, "Sound/pew_pew.mp3")

SHOOT_SOUND_ENEMY = os.path.join(IMG_DIR, "Sound/laser.mp3")

SKULL_SOUND = os.path.join(IMG_DIR, "Sound/mario_star.mp3")

POWER_SOUND = os.path.join(IMG_DIR, "Sound/minecraft_eat.mp3")

START_SOUND = os.path.join(IMG_DIR, "Sound/start.mp3")

LOSE_SOUND = os.path.join(IMG_DIR, "Sound/lose.mp3")

ENEMY_DEATH_SOUND = os.path.join(IMG_DIR, "Sound/roblox-death.mp3")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

FREEZE = pygame.image.load(os.path.join(IMG_DIR, 'Other/freeze2.png'))

SKULL = pygame.image.load(os.path.join(IMG_DIR, 'Other/skull.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

COVER_BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, 'Other/cover.png'))

COVER_SCORE = pygame.image.load(os.path.join(IMG_DIR, 'Other/cover_score.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
FREEZE_TYPE = 'freeze'
SKULL_TYPE = 'skull'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_SKULL = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_skull.png"))

BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))

ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'
