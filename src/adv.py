from room import Room
from player import Player
from item import Item

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

items = [Item('jeans', 'denim jeans'), Item('shirt', 'short sleeve shirt')]

items1 = [Item('knife', 'really big knife'), Item('pen', 'blue ink')]

items2 = [Item('taco', 'carne asada'), Item('paper', 'white paper')]

items3 = [Item('towel', 'green beach towel'), Item('camera', 'canon 5d')]

items4 = [Item('computer', 'laptop'), Item('shoes', 'adidas')]

room['outside'].items = items
room['foyer'].items = items1
room['overlook'].items = items2
room['narrow'].items = items3
room['treasure'].items = items4



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

## 

#this is setting  player.name and player.current_room
player = Player(input("What is your name?"), room['outside'])


print(f"Hello, {player.name} \n")
print(player.current_room)


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

valid_verbs = {'take', 'get', 'drop', 'i', 'inventory'}

while True:
    cmd = input("\n-->")
    if cmd == "q":
        print("GoodBye")
        exit(0)
    elif cmd in ("n", "s", "e", "w"):
        player.travel(cmd)
    elif cmd.split(" ")[0] in valid_verbs:
        verb = cmd.split(" ")[0] 
        if verb == 'take' or verb == 'get':
            item_name = cmd.split(" ")[1]
            print(player.on_take(item_name))
        elif verb == 'drop':
            item_name = cmd.split(" ")[1]
            print(player.on_drop(item_name))
        elif verb == 'i' or 'inventory':
            for item in player.items:
                print(item.name)
    else:
        print("i did not understand that command.")
