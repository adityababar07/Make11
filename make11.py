# Make 11 
# Started on 07:36 PM Saturday, December 02 2023


# modules

import random


#Level 1: A player is dealt 5 cards from a shuffled deck. The hand of cards is displayed in the console.

# used https://edukits.co/text-art/ to generate fancy console text.

print('''
==================================================================
 ooo        ooooo           oooo                         .o    .o  
 `88.       .888'           `888                       o888  o888  
  888b     d'888   .oooo.    888  oooo   .ooooo.        888   888  
  8 Y88. .P  888  `P  )88b   888 .8P'   d88' `88b       888   888  
  8  `888'   888   .oP"888   888888.    888ooo888       888   888  
  8    Y     888  d8(  888   888 `88b.  888    .o       888   888  
 o8o        o888o `Y888""8o o888o o888o `Y8bod8P'      o888o o888o 
                                                                   
==================================================================
''')

# let's create a matrix of cards  where cards in row 1 = hearts, row 2 = diamonds, row 3 = club, row 4 = spades.

cards = [[1,2,3,4,5,6,7,8,9,'K','Q','J'],
         [1,2,3,4,5,6,7,8,9,'K','Q','J'],
         [1,2,3,4,5,6,7,8,9,'K','Q','J'],
         [1,2,3,4,5,6,7,8,9,'K','Q','J']]


# player needs to have 5 random cards in hand

row = random.randint(0,3)
coloumn = random.randint(0, 11)

card = cards[row][coloumn]
print(card)



# the player has five cards so let's create a list with five cards

player_cards = []



#End