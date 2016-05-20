def string_decoder (recieved_string):
    

    categories = recieved_string.split('|')
    food_info = categories[0]
    player_info = categories[1]
    
    food_info = food_info.split('/')
    player_info = player_info.split('/')
# FOOD Decoding
    for i in range(len(food_info)):
        food_info[i] = food_info[i].split(',')
        for u in range(len(food_info[i])):
            food_info[i][u] = int(food_info[i][u])
    
#Player Decoding
    for i in range(len(player_info)):
        player_info[i] = player_info[i].split(';')
        player_info[i][0] = player_info[i][0].split(':')
        player_info[i][1] = player_info[i][1].split(',')
        for e in range(len(player_info[i][1])):
            player_info[i][1][e] = int(player_info[i][1][e])
        player_info[i][1] = tuple(player_info[i][1])
    for i in range(len(player_info)):
        for e in range(len(player_info[i][0])):
            player_info[i][0][e] = player_info[i][0][e].split(',')
            for u in range(len(player_info[i][0][e])):
                player_info[i][0][e][u] = int(player_info[i][0][e][u])

    return food_info,player_info

print string_decoder("200,400,0/100,350,1|300,245,50:250,245,40;255,255,255/600,150,200;255,255,255")
