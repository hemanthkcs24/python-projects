import sys
import pygame
from ship import Ship
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)  

        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Fill the screen with a background color
            self.screen.fill((230, 230, 230))
            self.ship.blitme() 

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
if __name__ == '__main__':
    # making a game instance and running the game.
    ai = AlienInvasion()
    ai.run_game()

    
    