from Food_Blobs import *
class Segment(food_blobs):
    def __init__(self, surface, player,camera):
        food_blobs.__init__(self, surface, player.x, player.y,player.mass, camera, player.color)
        self.mass = player.mass/2
        self.duration = 0

    def collision_detection(self, item_list, item_value, required_mass, camera):
        for item in item_list:
            if distance(self.x,self.y,item.x,item.y) <= self.mass/3 and self.mass > required_mass:
                item_list.remove(item)
                self.mass += 10*float(item_value)/self.mass
##                self.cameraValue += 10*float(item_value)/self.mass

    def fuse(self,player,segments):
        if int(self.velocity) == 0:
            self.x = player.x + player.mass/3 
            self.y = player.y + player.mass/3
        
        if self.duration >= 1000:
            player.mass += self.mass
            segments.remove(self)
            
    def explode(self,camera,viruses,food_blob_list):
        food_blob_size = (self.mass*0.7)/8
        segments = points_on_circumfrence(self.mass/3,7)
        angles = [(2*math.pi/7*x)*(self.mass/3) for x in xrange(0,8)]
        for i in range(8):
            x,y = segments[i]
            x += self.x
            y += self.y
            food_blob = food_blobs(self.surface,x,y,self.mass,camera,self.color)
            food_blob.angle = angles[i]
            food_blob_list.append(food_blob)
            self.mass = self.mass-food_blob_size
            self.cameraValue -= 5*float(food_blob_size)/self.mass

    def render(self,camera):
        pygame.draw.circle(self.surface,self.color,(int(self.x*camera.zoom+camera.x),int(self.y*camera.zoom+camera.y)),int(camera.zoom*self.mass/3),0)

    def update(self,player,segments,viruses,item_list, item_value, required_mass, camera):
        self.render(camera)
        self.move()
        self.collision_detection(item_list, item_value, required_mass, camera)
        self.fuse(player,segments)
        
def split(segments,surface,player,camera):
    if player.mass >= 32:
        segment = Segment(surface,player,camera)
        segments.append(segment)
        player.mass /= 2
