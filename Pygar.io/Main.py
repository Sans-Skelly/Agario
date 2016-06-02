import pygame
import random
import math
from Player import *
from Food import *
from Food_blobs import *
from Additional_Functions import *
from Camera import *
from labels_and_text import *

WHITE = (255,255,255)

screenWidth = 900
screenHeight = 900
screen=pygame.display.set_mode((screenWidth,screenHeight))
player = Player(screen,screenHeight,screenWidth)
camera = Camera(screenWidth,screenHeight)
food_list = []
food_blob_list = []
segments = []
spawn_food(food_list,450,screen,screenHeight+2100,screenWidth+2100)
pygame.key.set_repeat(1,2000)
inPlay = True

clock = pygame.time.Clock()

while inPlay: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
            if event.key == pygame.K_SPACE:   
                player.feed(food_blob_list,screenWidth,screenHeight,camera)
                
    camera.zoom = 1/(0.04*player.cameraValue) + 0.3
    camera.centre(player,screenWidth, screenHeight)
    
    screen.fill(WHITE)
    drawGrid(screen,screenWidth,screenHeight,camera)
    
    #Render Food Blobs
    for item in food_blob_list:
        item.update(camera)
        
    #Render Food Items
    for item in food_list:
        item.render(camera)
        
    player.update(food_list,food_blob_list,camera,screenWidth,screenHeight)
    render_score_label(screenWidth,screenHeight,player.mass,screen)
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
