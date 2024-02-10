import pygame
 
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
 
dialogue_font = pygame.font.SysFont('arial', 15)
name_font = pygame.font.SysFont('Helvetica', 20)
game_over_font = pygame.font.SysFont('Verdana', 60)
 
dialogue = dialogue_font.render("Hello World!",
                                True, (255,0,0))
name = name_font.render("Game programming with Python", True, (100,100,55))
game_over = game_over_font.render("Game Over", True, (0,0,255))
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    screen.fill((255, 255, 255))
     
    screen.blit(dialogue, (40,40))
    screen.blit(name, (40,140))
    screen.blit(game_over, (40,240))
     
    pygame.display.flip()
    clock.tick(60)