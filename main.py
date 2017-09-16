'''
Main file set up to run the game.
This file creates 4 rooms, 8 links, 3 enemies, 1 friend and 3 items.
It then runs the game until either the player wins or loses all their lives
'''
import rpg

# Helper functions
#

def start_displays():
    '''
    Helper function: prints out information to the player at the start of the game.
    Called after rooms, items, enemies and friend have been set up
    '''
    print('Welcome, brave adventurer!')
    print('You have ' + str(rpg.Room.get_num_rooms()) + ' rooms to explore.')
    print('To win the game, you must defeat ' + str(rpg.Enemy.get_num_enemies()) + ' enemies')
    print('If an enemy defeats you when you fight, you lose a life')
    print('You start the game with ' + str(rpg.Enemy.get_num_lives()) + ' lives')
    print('You also have ' + str(rpg.Item.get_num_items()) + ' weapons to make use of')
    print('You have a friend who can advise you on what weapons you need')
    print('You can also try to put an enemy to sleep, but that does not always succeed')
    print('Good luck!!!')
    print()

def process_fight(inhabitant, room, backpack, Enemy):
    '''
    Helper function which determines the outcome of a fight with an enemy.
    Inputs:  inhabitant, an enemy character
             room, the room inhabitant is in
             backpack, the weapons holder
             Enemy, a pointer to the Enemy class
    Returns: True if the game is over, otherwise False
    '''
    if len(backpack) == 0:
        print("You've no weapons to fight with yet!!")
        return False
    weapon_list = 'Choose your weapon to fight ' + inhabitant.get_name()
    weapon_list  += ' from '
    for item in backpack:
        weapon_list = weapon_list + item + ', '
    weapon_list = weapon_list[:-2] + ' '  # remove the final comma
    weapon = input(weapon_list)
    if weapon not in backpack:
        print("You don't have " + weapon + ' to fight with!')
        return False
    outcome = inhabitant.fight(weapon)  # conduct the fight
    if outcome:
        room.remove_character()  # remove enemy from the room
        if rpg.Enemy.get_num_enemies() < 1:  # true if all enemies killed
            print("Congratulations, you've won!!!")
            return True
        else:
            return False
    if rpg.Enemy.get_num_lives() < 1: # true if all lives lost
        print("Unfortunately you've died and lost the game.")
        return True
    return False

def enemy_choices(enemies):
    '''
    Sets up a string to display the available enemy names for use in advice processing
    Input:  enemies, a dictionary mapping enemy names to enemy objects.
    Returns: a string suitable for displaying the available enemy names
    '''
    if len(enemies) == 0:  # no enemies present
        return ''
    enemies_list = 'Choose from: '
    for enemy in enemies:
        enemies_list = enemies_list + enemy + ', '
    enemies_list = enemies_list[:-2] + ' ' # remove trailing comma
    return enemies_list

# Set up game rooms, items, enemies and friend    

# Set up kitchen
kitchen = rpg.Room('Kitchen')
kitchen.set_description('A dank and dirty room buzzing with flies.')
# Set up Dining hall
dining_hall = rpg.Room('Dining Hall')
dining_hall.set_description('A large room with ornate golden decorations on each wall.')
# Set up Ballroom
ballroom = rpg.Room('Ballroom')
ballroom.set_description('A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.')
# Set up bedroom
bedroom = rpg.Room('Bedroom')
bedroom.set_description('The master bedroom - huge 4 poster bed!')
# Link the 3 rooms together as per diagram in 2.6
# Add in a link to the bedroom in the top quadrant
kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(ballroom, 'west')
bedroom.link_room(kitchen, 'east')
bedroom.link_room(ballroom,'south')
# create and place items
item1 = rpg.Item('banana', 'A large yellow piece of fruit', 'small', 'light')
item2 = rpg.Item('sword', 'A massive steel sword', 'large', 'heavy')
item3 = rpg.Item('pineapple', 'A juicy piece of fruit', 'large', 'light')
dining_hall.set_item(item1)
kitchen.set_item(item2)
bedroom.set_item(item3)
# Set up and place enemies
#Dave
dave = rpg.Enemy('Dave', 'A smelly zombie')
dave.set_conversation("I'm simply to die for!")
dave.set_weakness(item3.get_name())
dining_hall.set_character(dave)
#Lucretia
lucretia = rpg.Enemy('Lucretia', 'A wicked and cunning witch')
lucretia.set_conversation("Look at my lovely blond hair.")
lucretia.set_weakness(item2.get_name())
kitchen.set_character(lucretia)
#Jamie
jamie = rpg.Enemy('Jamie', 'A vindictive poltergeist')
jamie.set_conversation("I hate humans sooo much!")
jamie.set_weakness(item1.get_name())
bedroom.set_character(jamie)
# create and place a friend character
casper = rpg.Friend('Casper', 'A cute, friendly ghost')
casper.set_conversation("I'm not three sheets in the wind... honest!")
ballroom.set_character(casper)
# Set up other requirements for game
current_room = kitchen  # start in the kitchen
backpack = []  # for storing items in
start_displays()

# main processing loop
game_over = False
while not game_over:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    print("Choose one of : north, south, east, west, talk, fight, sleep, advice, take")
    command = input("> ")
    if command in ('north', 'south', 'west', 'east'):  # player wants to move rooms
        current_room = current_room.move(command)
    elif command == 'talk':  # can only talk if room has an inhabitant
        if inhabitant:
            inhabitant.talk()
        else:
            print("There's no one to talk to here!")
    elif command == 'take':  # can only take item if it exists in this room
        item = current_room.get_item()
        if item:
            print('Adding item ' + item.get_name() + ' to backpack.')
            backpack.append(item.get_name())
            current_room.remove_item()
        else:
            print('No item in this room.')        
    elif command in ('fight', 'sleep'):  # only appropriate for enemy
        if isinstance(inhabitant, rpg.Enemy):
            if command == 'fight':
                game_over = process_fight(inhabitant, current_room, backpack, rpg.Enemy)
            else:  # player wants to send enemy to sleep
                inhabitant.sleep()
        else:
            print('You can only fight or put to sleep if there is an enemy in this room')
    elif command == 'advice':  # only appropriate for a friend
        if isinstance(inhabitant, rpg.Friend):
            enemies = rpg.Enemy.get_enemies()  # get the dictionary of enemies
            enemy = input(enemy_choices(enemies))
            if enemy in enemies:
                weakness = inhabitant.advice(enemy, enemies)
                if weakness:
                    print(weakness + ' is the weakness of enemy ' + enemy)
                else:
                    print("No weakness defined for " + enemy)
            else:
                print(enemy + ' is not an existing enemy')
        else:
            print('No friend here to give advice!!')
    else:  #  don't recognise command
        print("Don't recognise " + command +'\n')











                            
