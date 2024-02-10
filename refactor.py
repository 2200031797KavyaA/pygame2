from pygame.locals import *
import pygame
import time
from random import randint

# snake class
class Player:
    # horizontal position
    x = 0

    # vertical position
    y = 0 

    # direction
    d = 0

    # old positions
    positions = []

    # Size of snake
    length = 4

# apple class
class Apple:
    x = 0
    y = 0

# game class
class Game:
    game_width = 10
    game_height = 10
    grid_size = 44

    # collision detection
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

    def __init__(self):
        self._running = True

        # create player obj
        self.player = Player()

        # create apple obj
        self.apple = Apple()

        # set position
        self.apple.x = randint(0,self.game_width) * self.grid_size
        self.apple.y = randint(0,self.game_height) * self.grid_size

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((640,480), pygame.HWSURFACE)
        pygame.display.set_caption('Pygame example')

        # load images
        self._snake_image = pygame.image.load("snake.png").convert()
        self._apple_image = pygame.image.load("apple.png").convert()
       
    def on_render(self):
        self._display_surf.fill((0,0,0))
        #self._display_surf.blit(self._snake_image, (self.player.x,self.player.y)) 

        # draw snake
        for pos in self.player.positions:
            self._display_surf.blit(self._snake_image, (pos[0],pos[1])) 

        # draw apple
        self._display_surf.blit(self._apple_image, (self.apple.x,self.apple.y))

        # update screen
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()

    def snake_logic(self):
        if self.player.d == 0:
            self.player.x += 44
        elif self.player.d == 1:
            self.player.x -= 44
        elif self.player.d == 2:
            self.player.y -= 44
        elif self.player.d == 3:
            self.player.y += 44

        if len(self.player.positions) < self.player.length:
            self.player.positions.append((self.player.x,self.player.y))
        else:
            self.player.positions.pop(0)
            self.player.positions.append((self.player.x,self.player.y))

    def game_play_logic(self):
        if self.isCollision(self.player.x,self.player.y,self.apple.x,self.apple.y, 44):
            print('collides')
            self.apple.x = randint(0,self.game_width) * self.grid_size
            self.apple.y = randint(0,self.game_height) * self.grid_size
            self.player.length += 1

        if len(self.player.positions) > self.player.length-1:
            for i in range(0,self.player.length-1):                    
                if self.isCollision(self.player.x,self.player.y,self.player.positions[i][0], self.player.positions[i][1],40):
                    print('GAME OVER')
                    exit()      

    def game_logic(self):
        self.snake_logic()
        self.game_play_logic()                

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                
        keys = pygame.key.get_pressed() 
        
        if keys[K_RIGHT]:
            self.player.d = 0

        if keys[K_LEFT]:
            self.player.d = 1

        if keys[K_UP]:
            self.player.d = 2

        if keys[K_DOWN]:
            self.player.d = 3


    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while self._running:
            self.handle_events()
            self.game_logic()
            self.on_render()
            time.sleep(0.1)
  
        self.on_cleanup()
 
if __name__ == "__main__" :
    game = Game()
    game.on_execute()
