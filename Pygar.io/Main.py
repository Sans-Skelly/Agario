import pygame
import random
import math
from Player import *
from Food import *
from Food_Blobs import *
from Additional_Functions import *

WHITE = (255,255,255)

screenWidth = 1200
screenHeight = 1200
screen=pygame.display.set_mode((screenWidth,screenHeight))
player = Player(screen,screenHeight,screenWidth)
local_player_objects = [player]
food_list = []
food_blob_list = []
spawn_food(food_list,700,screen,screenHeight,screenWidth)

inPlay = True

clock = pygame.time.Clock()

while inPlay:
    screen.fill(WHITE)  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
            if event.key == pygame.K_SPACE:         
                player.feed(food_blob_list)
    screen.fill(WHITE)  
    #Render Food Blobs
    for item in range(len(food_blob_list)):
        food_blob_list[item].update()
    #Render Food Items
    for item in range(len(food_list)):
        food_list[item].render()
    #Update And Render Local Player Objects Food Items
    for item in range(len(local_player_objects)):    
        local_player_objects[item].update(food_list,food_blob_list)                
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()