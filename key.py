import pygame
import winsound

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

class Key():
    def __init__ (self, screen, note, key):
        self.y_point = 400
        self.note = note
        self.key = key
        self.width = 100
        self.height = 200
        self.screen = screen

    def draw(self, x_point):
        #it's just a white rectange
        #CHANGE T H I C C N E S S TO BLACK
        pygame.draw.rect(self.screen, BLACK, (x_point, self.y_point, self.width, self.height),5)
        pygame.draw.rect( self.screen,WHITE, (x_point, self.y_point, self.width, self.height),0)
        
    def play(self):
        #plays the Key
        #should darken key
        #if key on keyboard is played... play audio file
        # and also darken the key

        #figure out how to make k_[self.key]
        #temp is C
        
#HAD TO HARD CODE THE X_POINT !!!
#WHY IS IT RANDOMLY BECOMING BLACK?????
        if pygame.key.get_pressed()[pygame.K_c] != 0:
            pygame.draw.rect( self.screen,BLACK, (0, self.y_point, self.width, self.height),0)
            winsound.PlaySound(self.note,winsound.SND_FILENAME)
        

        
    
