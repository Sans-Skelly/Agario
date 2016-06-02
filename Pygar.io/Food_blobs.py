import pygame
from Additional_Functions import *

class food_blobs:
    def __init__(self, surface, player_X, player_Y,player_mass, camera, player_color):     
        self.color = player_color
        self.surface = surface
        self.acceleration = 0.65
        self.velocity = 16
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        self.angle = get_angle(self.mouseX,self.mouseY,int(player_X*camera.zoom+camera.x),int(player_Y*camera.zoom+camera.y))
        self.points_on_circumfrence = points_on_circumfrence(player_mass/3)
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
        if self.x < 12:
            self.x = 12
        elif self.x > (3000-(12)):
            self.x = (3000-(12)) 
            
        if self.y < 12:
            self.y = 12 
        elif self.y > (3000-(12)):
            self.y = (3000-(12))        
        
    def render(self,camera):
        pygame.draw.circle(self.surface,self.color,(int(self.x*camera.zoom+camera.x),int(self.y*camera.zoom+camera.y)),int(camera.zoom*8))

    def update(self,camera):
        self.render(camera)
        self.move()
