from room import Room
from player import Player
import textwrap 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].connections["n"] = room['foyer']
room['foyer'].connections["s"] = room['outside']
room['foyer'].connections["n"] = room['overlook']
room['foyer'].connections["e"] = room['narrow']
room['overlook'].connections["s"] = room['foyer']
room['narrow'].connections["w"] = room['foyer']
room['narrow'].connections["n"] = room['treasure']
room['treasure'].connections["s"] = room['narrow']

#
# Main
#




#Player creates name
name = input("Enter your name:")
# Make a new player object that is currently in the 'outside' room.
player_outside = Player(name, room['outside'])
# Write a loop that:

#current_room = Player(player_outside)

# * Prints the current room name
#for key in room:

# * Prints the current description (the textwrap module might be useful here).
wrapper = textwrap.TextWrapper(width=50)
#print(wrapper.wrap(room['outside']))
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Make a new player object that is currently in the 'outside' room.
player_outside = Player(name, room['outside'])
## set move to 0
move = 0
## set room to 'outside'
current_room = player_outside.current_room.name
# Write a loop that:
while not move == 9:  
# * Prints the current room named
    print(f'{name} you are currently in {current_room}')
# * Prints the current description (the textwrap module might be useful here).
# changed into a string
#print(f'{name} be aware that {room.current_room.description}')
    print(f'{name} be aware that {player_outside.current_room.description}')
# * Waits for user input and decides what to do.
    print(f'Choose were to move, a wrong move could cost you...')
    move = input("[n] North [e] East [s] South [w] West [9] Quit\n")
# If the user enters a cardinal direction, attempt to move to the room there.
    if move in ["n", "e", "s", "w"]:
        player_outside.goto(move)
    else:
        print("Wrong Move")
        move = 9


# current_room = room[current_room] + move
# print(current_room)
# print(f'You chose to move {room[current_room][move]}')
# new_room = room[current_room][move]
# print(new_room)
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#1. Player enters name
#2. Display room and description
#3. Give choice where to move, based upon options
# move = input("[1] North [2] East [3] South [4] West [9] Quit\n")
#4. After move, display room and description, repeat.
#5. end game with 9
