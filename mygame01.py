#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      move [direction]
      pick [item]
      attack [creature]  
    ''')

def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print('You are heading towards ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
      print('You see the ' + rooms[currentRoom]['item'])
    if "attack" in rooms[currentRoom]:
      print('You encounter the ' + rooms[currentRoom]['attack'])
    print("---------------------------")


#an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {

            'DoorWay' : {
                  'south' : 'Hall'
                },

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'east'  : 'Garden',
                  'item'  : 'Bat',
                  'attack' : 'Monster'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'west'  : 'Kitchen',
                  'item'  : 'Bow',
                  'attack' : 'Monster'
                },
            'Sheed' : {
                'east'  : 'Kitchen',
                'north' : 'Garage',
                'item'  : 'Backpack'
                },
            'Garage' : {
                'south' : 'Sheed',
                'east'  : 'Hall',
                'item'  : 'Cold Drink'
                },
            'Bedroom' : {
                'south east' : 'Dining Room',
                'north west' : 'Hall',
                'item'       : 'Gear'
            }
         }

#start the player in the DoorWay
currentRoom = 'DoorWay'

showInstructions()

#loop forever
while True:
    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'move east' would give the list:
    #['move','east']
    move = ''
    while move == '':  
        move = input('>')

    # split allows an items to have a space on them
    # pick golden key is returned ["pick", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'move' first
    if move[0] == 'move':
        #check that they are allowed wherever they want to move
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t move that way!')

    #if they type 'pick' first
    if move[0] == 'pick' :
        #if the room contains an item, and the item is the one they want to pick
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' collected!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to pick
        else:
            #tell them they can't get it
            print('Can\'t pick ' + move[1] + '!')

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
