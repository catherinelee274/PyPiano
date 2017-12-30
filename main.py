from time import sleep
import pygame
import random
import winsound
from key import Key
from words import Words

pygame.init()

#colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

#Note and respective sound file
G4 = '334540__teddy-frost__g4.wav'

#screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

done = False

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#title on top of browser
pygame.display.set_caption("Piano Typing Game")

#define class variables
key1 = Key( screen, G4, "C")

#init list of words 
wordList = []

#Main Loop
w1 = Words(screen)

score = 0 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))       #pygame.key.name returns the char version of the key pressed        
            if pygame.key.name(event.key) == w1.wordList[0]: #if it matches the first char in word list
                print("true")
                w1.wordList.remove(pygame.key.name(event.key)); 
            else:
                print("false")
        

    #remember not to put another draw function before the screen fill
    screen.fill(WHITE)
    
    key1.draw(0)
    key1.play()
    
    wordList.append(w1)
    
    
    if len(w1.wordList) != 0:
        w1.draw()
        w1.drop()
    else:
        score +=1        
        w1 = Words(screen) 
        
    #displays score
    myfont = pygame.font.SysFont('Comic Sans MS' ,30)  
    textsurface = myfont.render("Score: "+str(score), False, (0,0,0))
    screen.blit(textsurface,(200,0))    


    
        
        
    #for elem in wordList:
        #elem.draw()
        #elem.drop()
        #print(elem.getY)
        #if(elem.getY == 500):
            #time.sleep(5)
            #w2 = Words(screen)
            #w2.drop()
            #wordList.append(w2)
            
    
        
    #if(len(wordList)) >5:
     #   wordList = wordList[:5]
    #if any element in wordlist hits floor add to array of words and when it gets to max, end game
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()
exit()
