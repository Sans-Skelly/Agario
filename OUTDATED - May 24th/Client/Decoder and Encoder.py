def recieving_decoder(recieved_string):
    """ (lst)(lst) -> (str)
    Decodes food info and player info from string into list.
    food_info format:    [[x,y,t],[x,y,t]]
    players_info format: [[[[x,y,t],[x,y,t]],(r,g,b),name],[[[x,y,m],[x,y,m]],(r,g,b),name]]
    String format:       'x,y,t/x,y,t|x,y,m:x,y,z;r,g,b;name/x,y,z:x,y,z;r,g,b;name'
    """

    categories = recieved_string.split('|')
    food_info = categories[0]
    players_info = categories[1]
    
    food_info = food_info.split('/')
    players_info = players_info.split('/')
    
# FOOD Decoding
    for i in range(len(food_info)):
        food_info[i] = food_info[i].split(',')
        for u in range(len(food_info[i])):
            food_info[i][u] = int(food_info[i][u])
    
#Player Decoding
    for i in range(len(players_info)):
        players_info[i] = players_info[i].split(';')
        players_info[i][0] = players_info[i][0].split(':')
        players_info[i][1] = players_info[i][1].split(',')
        for e in range(len(players_info[i][1])):
            players_info[i][1][e] = int(players_info[i][1][e])
        players_info[i][1] = tuple(players_info[i][1])
    for i in range(len(players_info)):
        for e in range(len(players_info[i][0])):
            players_info[i][0][e] = players_info[i][0][e].split(',')
            for u in range(len(players_info[i][0][e])):
                players_info[i][0][e][u] = int(players_info[i][0][e][u])

    return food_info,players_info

def sending_encoder(food_info,players_info):
    """ (lst)(lst) -> (str)
    Encodes food info and player info lists into sendable string.
    food_info format:    [[x,y,t],[x,y,t]]
    players_info format: [[[[x,y,t],[x,y,t]],(r,g,b),name],[[[x,y,m],[x,y,m]],(r,g,b),name]]
    String format:       'x,y,t/x,y,t|x,y,m:x,y,z;r,g,b;name/x,y,z:x,y,z;r,g,b;name'
    """
    
    #Food Encoding
    for i in range(len(food_info)):
        for e in range(len(food_info[i])):
            food_info[i][e] = str(food_info[i][e])
        food_info[i] = ','.join(food_info[i])
    food_info = '/'.join(food_info)

    #Player Encoding
    for i in range(len(players_info)):
        for e in range(len(players_info[i][0])):
            for u in range(len(players_info[i][0][e])):
                players_info[i][0][e][u] = str(players_info[i][0][e][u])
            players_info[i][0][e] = ','.join(players_info[i][0][e])
    for i in range(len(players_info)):
        players_info[i][1] = list(players_info[i][1]) #Change colour tuple to list
        print players_info[1]
        for e in range(len(players_info[i][1])):
            players_info[i][1][e] = str(players_info[i][1][e])
        players_info[i][1] = ','.join(players_info[i][1])
        players_info[i][0] = ':'.join(players_info[i][0])
        players_info[i] = ';'.join(players_info[i])
    players_info = '/'.join(players_info)
           
    return food_info+'|'+players_info 
