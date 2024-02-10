# Load modules
from pygame.locals import *
import pygame

# Define player class
class Player:
    x = 0
    y = 0 

# Game class
class Game:
    def __init__(self):
        self._running = True
        # Create player object
        self.player = Player()

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
        self._display_surf.blit(self._cat_image, (self.player.x,self.player.y)) 
        
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
                   
            # Handle keyboard events
            keys = pygame.key.get_pressed() 
            
            if keys[K_RIGHT]:
                self.player.x += 1

            if keys[K_LEFT]:
                self.player.x -= 1

            if keys[K_UP]:
                self.player.y -= 1

            if keys[K_DOWN]:
                self.player.y += 1

            if keys[K_a]:
                print('a')

            if keys[K_b]:
                print('b')
                
            # Update screen
            self.on_render()
  
        self.on_cleanup()
 
if __name__ == "__main__" :
    game = Game()
    game.on_execute()
