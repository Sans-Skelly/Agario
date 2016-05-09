import pygame
import random
from Food_Blobs import *
from Additional_Functions import *

class Player:
    def __init__(self,surface,screenHeight,screenWidth,name = "Unamed Cell"):
        self.x = random.randint(25,screenHeight - 25)
        self.y = random.randint(25,screenWidth - 25)
        self.mass = 40
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.name = name
        self.surface = surface
        self.Xspeed = 0
        self.Yspeed = 0
        
    def move(self):
        VELOCITY = 5-(self.mass*0.006)
        if VELOCITY <= 2.5:
            VELOCITY = 2.5
            
        mouseX, mouseY = pygame.mouse.get_pos()
        
        try:
            angle = get_angle(mouseX,mouseY,self.x,self.y)
            self.Xspeed = int((VELOCITY*math.cos(angle*math.pi/180))) 
            self.Yspeed = int((VELOCITY*math.sin((angle + 180)*math.pi/180)))
            if distance(mouseX,mouseY,self.x,self.y)<10:
                self.Xspeed = 0
                self.Yspeed = 0
                self.x,self.y = pygame.mouse.get_pos()
        except ZeroDivisionError:
            self.x,self.y = pygame.mouse.get_pos()
            self.Xspeed = 0
            self.Yspeed = 0
            
        self.x += self.Xspeed
        self.y += self.Yspeed

    def collision_detection(self, item_list, item_value, required_mass):
        for item in item_list:
            if distance(self.x,self.y,item.x,item.y) <= self.mass/2 and self.mass > required_mass:
                item_list.remove(item)
                self.mass += item_value

    def feed(self,food_blob_list):
        if self.mass >= 36:
            food_blob = food_blobs(self.surface,self.x,self.y,self.Xspeed,self.Yspeed,self.color)
            food_blob_list.append(food_blob)
            self.mass = self.mass-16
        
        else:
            pass

    def massLoss(self):
        if self.mass >= 250:
            pass
        else:
            pass
        
    def render(self):
        pygame.draw.circle(self.surface,self.color,(self.x,self.y),self.mass/2, 0)

    def update(self,food_list,food_blob_list):
        self.massLoss()
        self.move()
        self.collision_detection(food_list,1,1)
        self.collision_detection(food_blob_list,12,40)
        self.render()
