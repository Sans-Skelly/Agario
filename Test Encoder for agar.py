

def client_encoder(eaten_food_coords, blobs, clr):
    """Format for eaten food coords and blobs is [[x,y,m],[x,y,m]]
    """
    string_eaten_food_coords = []
    for item in eaten_food_coords:
        for i in range(len(item)):
            item[i] = str(item[i])
        string_eaten_food_coords.append(','.join(item))
    formated_eaten_food_coords = '/'.join(string_eaten_food_coords)

    string_blobs = []
    for item in blobs:
        for i in range(len(item)):
            item[i] = str(item[i])
        string_blobs.append(','.join(item))
    formated_blobs = ':'.join(string_eaten_food_coords)

    clr_list = []
    for i in range(len(clr)):
        clr_list.append(str(clr[i]))
    formated_clr = ','.join(clr_list)
    
    return formated_eaten_food_coords+'|'+formated_blobs+'|'+formated_clr 
        
print client_encoder([[1,2,3],[2,3,4]], [[1,2,10],[1,2,10]],(255,255,255))
