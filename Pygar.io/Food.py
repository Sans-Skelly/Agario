import random
import pygame

class Food:
    def __init__(self,surface,screenHeight,screenWidth):
        self.x = random.randint(25,screenWidth-25)
        self.y = random.randint(25,screenHeight-25)
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.surface = surface
             
    def render(self,camera):
        pygame.draw.circle(self.surface,self.color,(int(self.x*camera.zoom+camera.x),int(self.y*camera.zoom+camera.y)),int(camera.zoom*4))
            
def spawn_food(food_list,num_of_food_elements,surface,screenHeight,screenWidth):
    for element in range(num_of_food_elements):
        food = Food(surface,screenHeight,screenWidth)
        food_list.append(food)
