import pygame
class Camera:
    def __init__(self, screenWidth, screenHeight):
        self.x = 0
        self.y = 0
        self.Xspeed = 0
        self.Xspeed = 0
        self.width = screenWidth
        self.height = screenHeight
        self.zoom = 10.0

    def centre(self,player,screenWidth,screenHeight):
        self.x = (screenWidth/2)-(player.x*self.zoom)
        self.y = (screenHeight/2)-(player.y*self.zoom)
            
