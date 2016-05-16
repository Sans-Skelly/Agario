def string_decoder (recieved_string):
    

    categories = recieved_string.split('|')
    food_info = categories[0]
    player_info = categories[1]
    
    food_info = food_info.split('/')
    player_info = player_info.split('/')

    for i in range(len(food_info)):
        food_info[i] = food_info[i].split(',')
        for u in range(len(food_info[i])):
            food_info[i][u] = int(food_info[i][u])
    




    return food_info
print string_decoder("200,400,0/100,350,1|300,245,50:250,245,40;255,255,255/600,150,200;255,255,255")
