# Week 2 Challenge - Item class
#

class Item():
    '''
    Class to represent a simple item which might be found in a room.
    '''

    num_items = 0  # keeps track of total items in game
    
    def __init__(self, name=None, description=None, size=None, weight=None):
        '''
        Constructor to initialise an item object
        Inputs:  name, the name of the item
                 description, textual description of the item
                 length, the size of the item (small or large)
                 weight, the weight of the item (light or heavy)
        '''
        # Validate size and weight parameters if provided
        if size:
            assert size in ('small', 'large')
        if weight:
            assert weight in ('light', 'heavy')
        self.name = name
        self.description = description
        self.size = size
        self.weight = weight
        Item.num_items += 1
 
    # getters

    def get_name(self):
        '''
        Returns item's name
        '''
        return self.name

    def get_description(self):
        '''
        Returns item's description
        '''
        return self.description

    def get_size(self):
        '''
        Returns item's size
        '''
        return self.size

    def get_weight(self):
        '''
        Returns item's weight
        '''
        return self.weight

    def get_details(self):
        '''
        Returns a string giving a full description of the item
        which is suitable for printing.
        '''
        description = ''
        description += 'Item ' + str(self.name)+ '\n'
        description += '-' * (5 + len(str(self.name))) + '\n'
        description += 'Description: ' + str(self.description) + '\n'
        description += 'Size: ' + str(self.size) + '\n'
        description += 'Weight: ' + str(self.weight) + '\n'
        return description

    @staticmethod
    def get_num_items():
        '''
        Returns the number of items in the game
        '''
        return Item.num_items

    # setters

    def set_name(self, name):
        '''
        Updates the item's name with name provided
        '''
        self.name = name

    def set_description(self, description):
        '''
        Updates the item's description with description provided
        '''
        self.description = description

    def set_size(self, size):
        '''
        Updates item's size. Fails if size provided not 'small' or 'large'
        '''
        assert size in ('small', 'large')
        self.size = size

    def set_weight(self, weight):
        '''
        Updates item's weight. Fails if weight provided not 'light' or 'heavy'
        '''
        assert weight in ('light', 'heavy')
        self.weight = weight
    
