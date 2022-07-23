import pygame
from settings import Settings
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_game):
        """Initializes the ship and sets its initial position"""
        super().__init__()
        self.screen = ai_game
        self.settings = Settings()
        self.screen_rect = ai_game.get_rect()

        self.image = pygame.image.load('images/3.bmp')
        self.rect = self.image.get_rect()

        # Every new ship respawn bottom edge screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # Move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """updates the ship's position based on the flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """draws the ship at the current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
