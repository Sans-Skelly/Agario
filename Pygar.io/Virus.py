import pygame
import random
class Virus(object):
    def __init__(self,surface,screenHeight,screenWidth):
        """ (object),(object),(int),(int) ---> (None) 
        """
        self.x = random.randint(25,screenHeight - 25)
        self.y = random.randint(25,screenWidth - 25)
        self.mass = 100
        self.color = (173,255,47)
        self.borderColor = (34,139,34)
        self.surface = surface
        
    def render(self,camera):
        """ (object),(object) ---> (None) 
        """
        x = int(self.x*camera.zoom+camera.x)
        y = int(self.y*camera.zoom+camera.y)
        pygame.draw.circle(self.surface,self.color,(x,y),int(self.mass/2*camera.zoom), 0)
        pygame.draw.circle(self.surface,self.borderColor,(x,y),int(self.mass/2*camera.zoom),15)

    def update(self,camera):
        """ (object),(object) ---> (None) 
        """
        self.render(camera)
