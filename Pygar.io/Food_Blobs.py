import pygame

class food_blobs:
    def __init__(self, surface, player_X, player_Y, player_Xspeed, player_Yspeed, player_color):
        self.x = player_X
        self.y = player_Y
        self.Xspeed = player_Xspeed + 2
        self.Yspeed = player_Yspeed + 2
        self.color = player_color
        self.surface = surface
        self.acceleration = 0.5
        
    def move(self):
        self.x += self.Xspeed
        self.y += self.Yspeed
        
    def render(self):
        pygame.draw.circle(self.surface,self.color,(self.x,self.y),16)

    def update(self):
        self.move()
        self.render()
        
