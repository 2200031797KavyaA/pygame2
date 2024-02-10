# Load modules
from pygame.locals import *
import pygame

# Game class
class Game:
    def __init__(self):
        self._running = True

    def on_init(self):
        # Init pygame, set window and title
        pygame.init()
        self._display_surf = pygame.display.set_mode((640,480), pygame.HWSURFACE)
        pygame.display.set_caption('Pygame example')

        # Load image
        self._cat_image = pygame.image.load("cat.jpg").convert()
       
    def on_render(self):
        # Clear screen
        self._display_surf.fill((0,0,0))

        # Show image
        self._display_surf.blit(self._cat_image, (0,0)) 
        
        # Update screen
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        # Game loop
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                   
            # Update screen
            self.on_render()
  
        self.on_cleanup()
 
if __name__ == "__main__" :
    game = Game()
    game.on_execute()
