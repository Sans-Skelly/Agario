import pygame
import random
#from Food_Blobs import *
from Additional_Functions import *
#from labels_and_text import *

class Player:
    def __init__(self,surface,screenHeight,screenWidth,name = "Unamed Cell"):
        self.x = random.randint(25,screenHeight - 25)
        self.y = random.randint(25,screenWidth - 25)
        self.mass = 16
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.name = name
        self.surface = surface
        self.Xspeed = 0
        self.Yspeed = 0
        self.label = myfont.render(self.name,1,(0,0,0))
        self.label_offset = self.label.get_width()
        
    def move(self):
        speed_percentage = 1-(self.mass*0.0012)
        if speed_percentage <= 0.25:
                    speed_percentage = 0.25 
                    
        mouseX, mouseY = pygame.mouse.get_pos()
        
        dx = mouseX - self.x
        dy = mouseY - self.y
    
        self.Xspeed = int(dx/20)       
        if self.Xspeed > 9:
            self.Xspeed = 9
        elif self.Xspeed < -9:
                        self.Xspeed = -9     
        self.Xspeed = int(speed_percentage * self.Xspeed)
        
        self.Yspeed = int(dy/20)
        if self.Yspeed > 9:
                    self.Yspeed = 9
        elif self.Yspeed < -9:
                        self.Yspeed = -9                  
        self.Yspeed = int(speed_percentage * self.Yspeed)
        self.x += self.Xspeed
        self.y += self.Yspeed    

##    def collision_detection(self, item_list, item_value, required_mass):
##        for item in item_list:
##            if distance(self.x,self.y,item.x,item.y) <= self.mass/2 and self.mass > required_mass:
##                item_list.remove(item)
##                self.mass += item_value
##
##    def feed(self,food_blob_list):
##        if self.mass >= 36:
##            food_blob = food_blobs(self.surface,self.x,self.y,self.mass+16,self.Xspeed,self.Yspeed,self.color)
##            food_blob_list.append(food_blob)
##            self.mass = self.mass-16
##        
##        else:
##            pass
##
##    #def split(self,surface,screenHeight,screenWidth,self.name):
##        #if self.mass >= 36:
##            #self.mass -= 16
##            #player = Player(surface,screenHeight,screenWidth,self.name)
##            
##    def massLoss(self):
##        if self.mass >= 250:
##            pass
##        else:
##            pass
        
    def draw(self):
        pygame.draw.circle(self.surface,self.color,(self.x,self.y),self.mass/2, 0)
        myfont = pygame.font.SysFont("monospace",int(self.mass/16))
        self.label = myfont.render(self.name,1,(0,0,0))
        self.label_offset = self.label.get_width()
        self.surface.blit(self.label, (self.x - (self.label_offset/2),self.y))
        
    def update(self,food_list,food_blob_list):
##        self.massLoss()
        self.move()
##        self.collision_detection(food_list,1,1)
##        self.collision_detection(food_blob_list,12,16)
