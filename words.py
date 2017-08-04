from random_words import RandomWords
import pygame

class Words():
    def __init__(self, screen):
        self.screen = screen
        
    def drop(self):
        rw = RandomWords()
        word = rw.random_word()
        myfont = pygame.font.SysFont('Comic Sans MS' ,30)
        textsurface = myfont.render(word, False, (0,0,0))
        self.screen.blit(textsurface,(0,0))
