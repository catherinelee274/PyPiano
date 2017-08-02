
import pygame
import random
from key import Key

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

done = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Piano Typing Game")

key1 = Key( screen, "A", "C" )


#Main Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #remember not to put another draw function before the screen fill
    screen.fill(WHITE)
    
    key1.draw(0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
