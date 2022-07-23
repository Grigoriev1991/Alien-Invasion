class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 100, 150)

        # Ship settings
        self.ship_limit = 3

        # Alien settings
        self.fleet_drop_speed = 5

        # Bullet option
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_allowed = 3
        self.bullet_color = (60, 60, 60)

        # Game acceleration rate
        self.speedup_scale = 1.2

        # Alien value growth rate
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Settings that change during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.5
        self.fleet_direction = 1  # Move to the right

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

