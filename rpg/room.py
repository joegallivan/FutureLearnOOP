# Week 2 - Room class
#
class Room():
    '''
    Blueprint for a room object in the adventure game.
    '''
    num_rooms = 0  # keep track of total number of rooms

    def __init__(self, room_name):
        '''
        Constructor - sets up instance variables and names the room
        Inputs:  room_name, the name of the room. Should be unique in the game.
        '''
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        Room.num_rooms += 1

    def set_description(self, room_description):
        '''
        Sets the description of the room.
        Inputs:  room_description, a textual description of the room
        '''
        self.description = room_description

    def get_description(self):
        '''
        Gets the description of the room
        Returns:  the room description.
        '''
        return self.description

    def set_character(self, new_character):
        '''
        Places a character in a room.
        Inputs:  new_character, a character object
        '''
        self.character = new_character

    def get_character(self):
        '''
        Gets the character in the room, if present
        Returns:  the character or None if none present.
        '''
        return self.character


    def set_item(self, new_item):
        '''
        Places an item in a room.
        Inputs:  new_item, an item object
        '''
        self.item = new_item

    def get_item(self):
        '''
        Gets the item in the room, if present
        Returns:  the item or None if none present.
        '''
        return self.item

    def remove_item(self):
        '''
        Removes the item from the room
        '''
        self.item = None

    def remove_character(self):
        '''
        Removes the character from the room
        '''
        self.character = None


    def set_name(self, room_name):
        '''
        Sets the name of the room.
        Inputs:  room_name, the room's name
        '''
        self.description = room_description

    def get_name(self):
        '''
        Gets the name of the room
        Returns:  the room's name.
        '''
        return self.name

    @staticmethod
    def get_num_rooms():
        '''
        Gets the number of rooms in the game
        '''
        return Room.num_rooms

    def describe(self):
        '''
        prints out the room's description
        '''
        print(self.description)

    def link_room(self, room_to_link, direction):
        '''
        Links a room and its direction from this room to the room supplied.
        The room to be linked to must already exist.
        Also links this room appropriately from the room just linked to.
        Inputs:  room_to_link, the room to link to this one.
                 direction, the direction from this room to the linked room.
                 Fails if direction not one of 'north', 'south', 'east, 'west'.
        '''
        assert direction in ('north', 'south', 'east', 'west')
        self.linked_rooms[direction] = room_to_link
        pairs = {'north':'south', 'south':'north', 'east':'west', 'west':'east'}
        room_to_link.linked_rooms[pairs[direction]] = self

    def list_linked_rooms(self):
        '''
        Prints out each room linked from this one and its direction
        '''
        if self.linked_rooms:
            for linked_room in self.linked_rooms:
                print('The ' +
                      self.linked_rooms[linked_room].get_name() +
                      ' is ' + linked_room)
        else:
            print('No links from this room')

    def get_details(self):
        '''
        Prints out full details of this room, including its links
        and any character or item present
        '''
        print('The ' + self.name)
        print('-' * (6 + len(self.name)))
        self.describe()
        self.list_linked_rooms()
        if self.character:
            self.character.describe()
        if self.item:
            print(self.item.get_details())

    def move(self, direction):
        '''
        Moves the player to the room in the relevant direction if possible.
        If the direction is not valid for this room, outputs a message and
        leaves the player in the current room.
        Inputs:  direction, the direction to move in (east, west, north or south)
        Returns:  the room moved to as a result of the move.
        '''
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self


              
    
                  
        
        
    
