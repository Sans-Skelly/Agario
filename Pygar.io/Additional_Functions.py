import math
import pygame

def distance(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

def get_angle(x1,y1,x2,y2):
    hyp = distance(x1,y1,x2,y2)
    adj = x2-x1
    angle = 180 + (math.acos(adj/hyp))/(math.pi/180)
    if y2>y1:
        angle = 180 - (math.acos(adj/hyp))/(math.pi/180)
    return angle

def drawGrid(surface,screenWidth,screenHeight,camera):
    GRIDSIZE = 50
    BLACK = (0,0,0)
    start = 0
    end = 3000
    for i in range(start,end+1,GRIDSIZE):
        pygame.draw.line(surface,BLACK,(start + camera.x,i*camera.zoom+camera.y),(end*camera.zoom+camera.x,i*camera.zoom+camera.y),1)
        pygame.draw.line(surface,BLACK,(i*camera.zoom+camera.x,start + camera.y),(i*camera.zoom+camera.x,end*camera.zoom+camera.y),1)
        
def points_on_circumfrence(r,n=359):
    r += 12
    segment_list = [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in xrange(0,n+1)]
    return segment_list
