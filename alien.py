import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """One Alien"""

    def __init__(self, ai_game):
        """Sets the starting position and initializes the alien"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/0.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien located at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
