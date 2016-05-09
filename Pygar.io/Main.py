import pygame
import random
import math
from Player import *
from Food import *
from Food_Blobs import *
from Additional_Functions import *

WHITE = (255,255,255)

screenWidth = 800
screenHeight = 800
screen=pygame.display.set_mode((screenWidth,screenHeight))
player = Player(screen,screenHeight,screenWidth)
food_list = []
food_blob_list = []
spawn_food(food_list,300,screen,screenHeight,screenWidth)

inPlay = True

clock = pygame.time.Clock()

while inPlay:
    pygame.event.get()
    keys = pygame.key.get_pressed()     # get_pressed() method generates a True/False list
                                        # for the status of all keys
    if keys[pygame.K_ESCAPE]:           
        inPlay = False
    if keys[pygame.K_LSHIFT]:           
        player.feed(food_blob_list)

    screen.fill(WHITE)
    player.update(food_list,food_blob_list)
    
    #Render Food Blobs
    for item in range(len(food_blob_list)):
        food_blob_list[item].update()
    #Render Food Items
    for item in range(len(food_list)):
        food_list[item].render()
        
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
