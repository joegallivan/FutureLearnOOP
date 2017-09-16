
from random import randint
class Character():
    '''
    Character class - a character in the game
    '''
    def __init__(self, char_name, char_description):
        '''
        Initialises variables.
        Inputs: char_name, the character's name
                char_description, a description of the character
        '''
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        '''
        Prints out the character's name and description
        '''
        print( self.name + " is here!" )
        print( self.description )

    def get_name(self):
        '''
        Returns the character's name
        '''
        return self.name

    def set_conversation(self, conversation):
        '''
        Set what this character will say when talked to
        '''
        self.conversation = conversation

    def talk(self):
        '''
        Prints out character's conversation
        '''
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    
    def fight(self, combat_item):
        '''
        prints out message saying character doesn't want fight
        '''
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    '''
    Enemy class - you fight against these!
    '''

    num_enemies = 0
    num_lives = 0  # keep track of number of enemies and lives
    enemies = {}  # maps names to enemy objects for all enemies

    def __init__(self, char_name, char_description):
        '''
        Constructor -calls super class's and creates a weakness attribute.
        '''
        super().__init__(char_name, char_description)
        assert char_name not in Enemy.enemies  # name must be unique
        self.weakness = None
        self.asleep = False  # week 3 challenge 3 addition
        Enemy.num_enemies += 1
        Enemy.num_lives += 1  # update numbers of lives and enemies
        Enemy.enemies[char_name] = self

    def set_weakness(self, weakness):
        '''
        Puts a value in weakness
        '''
        self.weakness = weakness


    def get_weakness(self):
        '''
        Returns weakness
        '''
        return self.weakness

    @staticmethod
    def get_num_enemies():
        '''
        Returns current number of enemies in the game
        '''
        return Enemy.num_enemies

    @staticmethod
    def get_num_lives():
        '''
        Returns current number of player's lives left
        '''
        return Enemy.num_lives

    @staticmethod
    def get_enemies():
        '''
        Returns the enemies dictionary mapping names to enemies
        '''
        return Enemy.enemies

    def remove_enemy(self, enemy):
        '''
        Removes the enemy with this name from the enemies dictionary.
        No effect if it is not in the dictionary
        Input:  enemy, the name of the enemy to be removed
        '''
        if Enemy.enemies.get(enemy):
            del Enemy.enemies[enemy]


    def fight(self, combat_item):
        '''
        Simulates a fight with this enemy character.
        If this enemy is asleep, player wins and enemy killed without a fight.
        If the combat item matches this enemy's weakness, caller wins.
        Otherwise, this enemy wins. In each case, a suitable message is printed.
        Updates number of lives, dictionary and number of enemies appropriately.
        Inputs:  combat_item, the weapon caller is using.
        Returns: True if caller wins, False if this enemy wins
        '''
        if self.asleep:
            self.asleep = False  # only lasts one round
            print(self.name + " was fast asleep, so killed without a fight!")
            Enemy.num_enemies -= 1
            self.remove_enemy(self.name)
            return True
        elif combat_item == self.weakness:
            print("You kill " + self.name + " with the " + combat_item )
            Enemy.num_enemies -= 1
            self.remove_enemy(self.name)
            return True
        else:
            print(self.name + " defeats you, puny adventurer")
            Enemy.num_lives -= 1
            return False

    def sleep(self):
        '''
        Allows a player to attempt to put this enemy character to sleep.
        If it succeeds, the player can fight it and will win the next bout.
        The player is unaware of the outcome.
        Returns: True if the attempt succeeds, otherwise False
        '''
        outcome = randint(1,2)
        if outcome == 1:
            self.asleep = True
        else:
            self.asleep = False
            

class Friend(Character):
    '''
    Advises player about enemy's weapons.
    '''

    # Constructor -calls super class's and creates a weakness attribute
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)


    def advice(self, enemy, enemies):
        '''
        Advises player about the weakness of an enemy.
        Inputs:  enemy, the name of an enemy
                 enemies, a dictionary mapping enemy name to its object
        Returns:  the weakness of this enemy
        '''
        return enemies[enemy].get_weakness()
    
        
    
        


    


