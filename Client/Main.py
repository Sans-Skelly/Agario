#General Modules
import pygame
import random
import math
from socket import *
import threading
import Queue
#Other Files
from client_socket import *
from Player import *

##from Food import *
##from Food_Blobs import *
##from Additional_Functions import *
##from labels_and_text import *

##########################################################
#--------------------Game Variables----------------------#
##########################################################

WHITE = (255,255,255)
screenWidth = 900
screenHeight = 900
screen=pygame.display.set_mode((screenWidth,screenHeight))
player = Player(screen,screenHeight,screenWidth)
player_objects = [player]
##food_list = []
##food_blob_list = []
##spawn_food(food_list,700,screen,screenHeight,screenWidth)
inPlay = True
clock = pygame.time.Clock()

##########################################################
#----------------Networking Variables--------------------#
##########################################################

PORT = 3000                             # arbitrary non-privileged port, same as on the server
BUFFER_SIZE = 1024                      # maximum amount of data that can be received at once
SERVER_IP = '192.168.1.38'

socket = socket(AF_INET, SOCK_DGRAM)
socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
socket.bind(('',PORT))

##########################################################
#-----------------Networking Startup---------------------#
##########################################################

print 'CLIENT '+computer_number+': Setting up Queues...'
recieving_q = Queue.Queue(10)
sending_q = Queue.Queue(10)
print 'CLIENT '+computer_number+': Queues setup.'

print 'CLIENT '+computer_number+': Starting recieving thread...'
recieving = Recieve(recieving_q,socket,BUFFER_SIZE)
recieving.start()
print 'CLIENT '+computer_number+': Started recieving thread.'

print 'CLIENT '+computer_number+': Starting sending thread...'
sending = Send(sending_q,socket,SERVER_IP,PORT)
sending.start()
print 'CLIENT '+computer_number+': Started sending thread.'

##########################################################
#-----------------------Functions------------------------#
##########################################################

def redraw_screen():
    screen.fill(WHITE)
    for player in player_objects:
        player.draw(food_list,food_blob_list)
    pygame.display.update()

##########################################################
#---------------------Main Program-----------------------#
##########################################################
    
while inPlay:  
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
##            if event.key == pygame.K_SPACE:         
##                player.feed(food_blob_list)
    
    #Render Food Blobs
##    for item in range(len(food_blob_list)):
##        food_blob_list[item].update()
##    #Render Food Items
##    for item in range(len(food_list)):
##        food_list[item].render()

    for player in player_objects:    
        player.update(food_list,food_blob_list)
        
    ##render_score_label(screenWidth,screenHeight,player.mass,screen)
    
    clock.tick(45)
    
pygame.quit()
