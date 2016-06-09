import pygame
import random
import math
from Player import *
from Food import *
from Food_Blobs import *
from Additional_Functions import *
from Camera import *
from labels_and_text import *
from Segment import *
from Virus import *

WHITE = (255,255,255)

screenWidth = 900
screenHeight = 900
screen=pygame.display.set_mode((screenWidth,screenHeight))
player = Player(screen,screenHeight,screenWidth)
camera = Camera(screenWidth,screenHeight)
food_list = []
food_blob_list = []
segments = []
viruses = [Virus(screen,screenHeight,screenWidth) for i in range(5)]
spawn_food(food_list,1000,screen,screenHeight+2100,screenWidth+2100)
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
            if event.key == pygame.K_LSHIFT and segments == []:   
                split(segments,screen,player,camera)

    camera.zoom = 1/(0.04*player.cameraValue) + 0.3
    camera.centre(player,screenWidth, screenHeight)

    print player.mass,player.cameraValue
    
    screen.fill(WHITE)
    drawGrid(screen,screenWidth,screenHeight,camera)
    
    #Render Food Blobs
    for item in food_blob_list:
        item.update(camera)
        
    #Render Food Items
    for item in food_list:
        item.render(camera)

    #Render And Update Segments
    for segment in segments:
        segment.update(player,segments,food_list,1,1,camera)
        segment.duration += 1

    #Render And Render Player
    player.update(food_list,food_blob_list,viruses,camera,screenWidth,screenHeight)

    #Render And Update Viruses
    for virus in viruses:
        virus.update(camera)

    #Render Score Label
    render_score_label(screenWidth,screenHeight,player.mass,screen)
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
