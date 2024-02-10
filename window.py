# Load modules
from pygame.locals import *
import pygame

# Game class
class Game:
    def __init__(self):
        self._running = True

    def on_init(self):
        # Initialize pygame
        pygame.init()
        # Create window
        self._display_surf = pygame.display.set_mode((640,480), pygame.HWSURFACE)
        # Set window title
        pygame.display.set_caption('Pygame example')
       
    def on_render(self):
        # Clear screen
        self._display_surf.fill((0,0,0))
        # Update screen
        pygame.display.flip()
 
    def on_cleanup(self):
        # Quit pygame
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        # Game loop
        while self._running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    
            # Update screen
            self.on_render()
  
        self.on_cleanup()
 
if __name__ == "__main__" :
    game = Game()
    game.on_execute()
