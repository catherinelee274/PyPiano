from random_words import RandomWords
import pygame
import random

rw = RandomWords()

class Words():
    def __init__(self, screen):
        self.screen = screen
        self.x_point = random.randint(0,800)
        self.y_point = 0
        self.word = rw.random_word()

    def drop(self):
        #creates a new object
        myfont = pygame.font.SysFont('Comic Sans MS' ,30)

        #figure out where to put this
        self.y_point +=2

        #creates a new surface with text drawn on it
        textsurface = myfont.render(self.word, False, (0,0,0))

        self.screen.blit(textsurface,(self.x_point,self.y_point))
        
        #if self.y_point == 600:
            #self.y_point = 0
            #if either it reaches bottom or everything is typed out...
            #make it delete from list
            
        
