import pygame
from Additional_Functions import *

class food_blobs:
    def __init__(self, surface, player_X, player_Y,player_mass, player_Xspeed, player_Yspeed, player_color):     
        self.color = player_color
        self.surface = surface
        self.acceleration = 0.65
        self.velocity = 16
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.angle = get_angle(self.mouseX,self.mouseY,player_X,player_Y)
        self.points_on_circumfrence = points_on_circumfrence(player_mass/2)
        self.Xspeed = int((self.velocity*math.cos(self.angle*math.pi/180))) 
        self.Yspeed = int((self.velocity*math.sin((self.angle + 180)*math.pi/180))) 
        self.x,self.y = self.points_on_circumfrence[int(self.angle)-1]
        self.x,self.y = int(player_X + self.x),int(player_Y - self.y)
        
    def move(self): 
        self.x += self.Xspeed
        self.y += self.Yspeed        
        self.velocity = self.velocity * 0.965
        self.Xspeed = int((self.velocity*math.cos(self.angle*math.pi/180))) 
        self.Yspeed = int((self.velocity*math.sin((self.angle + 180)*math.pi/180)))        
        
    def render(self):
        pygame.draw.circle(self.surface,self.color,(self.x,self.y),12)

    def update(self):
        self.render()
        self.move()
        
