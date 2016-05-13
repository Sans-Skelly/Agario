##
def string_decoder (recieved_string):
    player = []
    food = []
    categories = recieved_string.split('|')
    food_info = categories[0].split('/')
    player_info = categories[1].split('/')
    for i in food_info:
        food.append(i.split(','))
    for i in player_info:
        player.append(i.split(','))
    return food, player
