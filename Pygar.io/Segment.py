from Food_blobs import *
class Segment(food_blobs):
    def __init__(self, surface, player,camera):
        food_blobs.__init__(self, surface, player.x, player.y,player.mass, camera, player.color)
        self.mass = player.mass/2
        self.duration = 0

    def collision_detection(self, item_list, item_value, required_mass, camera):
        for item in item_list:
            if distance(self.x,self.y,item.x,item.y) <= self.mass/2 and self.mass > required_mass:
                item_list.remove(item)
                self.mass += 10*float(item_value)/self.mass
##                self.cameraValue += 10*float(item_value)/self.mass

    def fuse(self,player,segments):
        if int(self.velocity) == 0:
            self.x = player.x + player.mass/2 
            self.y = player.y + player.mass/2
        
        if self.duration >= 1000:
            player.mass += self.mass
            segments.remove(self)

    def render(self,camera):
        pygame.draw.circle(self.surface,self.color,(int(self.x*camera.zoom+camera.x),int(self.y*camera.zoom+camera.y)),int(camera.zoom*self.mass/2),0)

    def update(self,player,segments, item_list, item_value, required_mass, camera):
        self.render(camera)
        self.move()
        self.collision_detection(item_list, item_value, required_mass, camera)
        self.fuse(player,segments)
        
def split(segments,surface,player,camera):
    segment = Segment(surface,player,camera)
    segments.append(segment)
    player.mass /= 2
