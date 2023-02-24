import sys
import pygame


class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.bg_color = (230, 230, 230)

        # Rocket settings
        self.rocket_speed = 1.5


class Rocket:
    """A class to manage the ship."""

    def __init__(self, rl_game):
        """Initialize the rocket and set its starting position."""
        self.screen = rl_game.screen
        self.settings = rl_game.settings
        self.screen_rect = rl_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load("images/pngwing.com.bmp")
        self.rect = self.image.get_rect()

        # Start each new rocket at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the rocket's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flags; start with a rocket that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


class RocketLeague:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Rocket League")

        self.rocket = Rocket(self)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rocket.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rocket.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    # Make a a game instance, and run the game.
    rl = RocketLeague()
    rl.run_game()
