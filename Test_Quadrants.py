import pygame
pygame.init()

class Quadrants():
    def __init__(self,rows,coloums,quad_length):
        self.rows = rows
        self.coloums = coloums
        self.quad_length = quad_length
        self.quadrants = []
        
        for i in range(self.rows):
            self.quadrants.append([])
            for e in range(self.coloums):
                quadrant_x = i*self.quad_length
                quadrant_y = e*self.quad_length
                self.quadrants[i].append(Quadrant([],quadrant_x,quadrant_y))

    def add_item(self,item):
        for coloum in self.quadrants:
            for quadrant in coloum:
                if quadrant.check(item) == (0,0):
                    quadrant.items.append(item)
                    break

    def update(self,quad_row,quad_coloum,item_ID,item_updated_x,item_updated_y,item_updated_m):
        item_index = self.quadrants[quad_row][quad_coloum].find(item_ID)
        if self.quadrants[quad_row][quad_coloum].check(self.quadrants[quad_row][quad_coloum].items[item_index]):
            self.quadrants[quad_row][quad_coloum].items[item_index].x = item_updated_x
            self.quadrants[quad_row][quad_coloum].items[item_index].y = item_updated_y
            self.quadrants[quad_row][quad_coloum].items[item_index].m = item_updated_m
        row_change,coloum_change = self.quadrants[quad_row][quad_coloum].check(self.quadrants[quad_row][quad_coloum].items[item_index])
        if row_change != 0 or coloum_change != 0:
            self.quadrants[quad_row][quad_coloum].items[item_index].quad_row = quad_row+row_change
            self.quadrants[quad_row][quad_coloum].items[item_index].quad_coloum = quad_coloum+coloum_change
            self.quadrants[quad_row+row_change][quad_coloum+coloum_change].items.append(self.quadrants[quad_row][quad_coloum].items[item_index])
            del self.quadrants[quad_row][quad_coloum].items[item_index]
        
        
    def draw(self,surface):
        for coloum in self.quadrants:
            for quadrant in coloum:
                quadrant.draw(surface)

class Quadrant():
    def __init__(self,items,x,y):
        self.items = items
        self.x = x
        self.y = y

    def check(self,item):
        if self.x > item.x: 
            if self.y > item.y:
                return -1,-1
            elif self.y + quad_length < item.y:
                return -1,1
            else:
                return -1,0

        elif self.x + quad_length < item.x:
            if self.y > item.y:
                return 1,-1
            elif self.y + quad_length < item.y:
                return 1,1
            else:
                return 1,0

        elif self.y > item.y:
            return 0,-1
        elif self.y+quad_length < item.y:
            return 0,1
        else:
            return 0,0    

    def find(self,item_ID):
        for i in range(len(self.items)):
            if self.items[i].ID == item_ID:
                return i

    def draw(self,surface):
        for item in self.items:
            pygame.draw.circle(surface,(0,0,0),(item.x,item.y),item.m/2, 0)
        if len(self.items) > 0:
            pygame.draw.rect(surface,(255,0,0),(self.x,self.y,quad_length,quad_length),2)
        else:
            pygame.draw.rect(surface,(0,0,0),(self.x,self.y,quad_length,quad_length),2)

class Client():
    def __init__(self,x,y,m,ID):
        self.quad_row = 0
        self.quad_coloum = 0
        self.x = x
        self.y = y
        self.m = m
        self.ID = ID


            
WHITE = (255,255,255)
screen_width = 900
screen_height = 900
screen=pygame.display.set_mode((screen_width,screen_height))
quad_length = 100
number_of_quad_rows = screen_width/quad_length
number_of_quad_coloums = screen_height/quad_length
inPlay = True

all_quadrants = Quadrants(number_of_quad_rows,number_of_quad_coloums,quad_length)

player_x = 10
player_y = 10
player_mass = 10

client = Client(player_x,player_y,player_mass,1)
all_quadrants.add_item(client)
    
def redraw_screen():
    screen.fill(WHITE)
    all_quadrants.draw(screen)
    pygame.display.update()
                
while inPlay:

    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x = player_x - 5
    if keys[pygame.K_RIGHT]:
        player_x = player_x + 5
    if keys[pygame.K_UP]:
        player_y = player_y - 5
    if keys[pygame.K_DOWN]:
        player_y = player_y + 5

    all_quadrants.update(client.quad_row,client.quad_coloum,1,player_x,player_y,player_mass)
    

##    for quadrant in all_quadrants:
##        if quadrant.check(client) == True:
##            quadrant.items

    redraw_screen()
    pygame.time.wait(30)
