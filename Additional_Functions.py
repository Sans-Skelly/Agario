import math

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

def points_on_circumfrence(r,n=359):
    r += 12
    segment_list = [(math.cos(2*math.pi/n*x)*r,math.sin(2*math.pi/n*x)*r) for x in xrange(0,n+1)]
    return segment_list