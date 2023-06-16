import pygame
from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, COVER_BACKGROUND, COVER_SCORE


class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (
            self.HALF_SCREEN_WIDTH+40, self.HALF_SCREEN_HEIGHT)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if event.type == pygame.KEYDOWN:
                game.run()

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def update_message(self, message):
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (
            self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def reset_screen_color(self, screen, death_count):
        # screen.fill((255,255,255))
        if death_count == 0:
            image = pygame.transform.scale(
                COVER_BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            image = pygame.transform.scale(
                COVER_SCORE, (SCREEN_WIDTH, SCREEN_HEIGHT))

        screen.blit(image, (0, 0))
