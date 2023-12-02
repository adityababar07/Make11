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

Rounds = 0
Score = 0

# the player has five cards so let's create a list with five cards

player_cards = []

# player needs to have 5 random cards in hand
no_of_cards = 0
while no_of_cards<5:
    row = random.randint(0,3)
    coloumn = random.randint(0, 11)
    card = [row, coloumn]
    if card not in player_cards:
        no_of_cards+=1
        player_cards.append(card)


# print(player_cards)

#gets computer's card

def computer_card():
    row = random.randint(0,3)
    coloumn = random.randint(0, 11)

    card = [row, coloumn]
    return card

#checks the suit of players card

def suit_check(card):
    if card == 0:
        suit = 'hearts'
    elif card== 1:
        suit = 'diamonds'
    elif card== 2:
        suit = 'club'
    else :
        suit = 'spade'
    
    return suit


# Display player's cards 
while True:
    Rounds += 1
    print(f'''
        -----------------Round {Rounds}-------------------
    ''')
    card = computer_card()

    while card in player_cards :
        card = computer_card()
    
    suit = suit_check(card)

    print(f'\ncomputer deals: {cards[card[0]][card[1]]} of {suit}\nCan you make it up to 11, or produce the same suit to continue the run?\n')
    
    print("Please choose a card from your hand to play\n")

    for i in range(5):
        print(f"{i+1}):{suit_check(player_cards[i][0])} of {cards[player_cards[i][0]][player_cards[i][1]]}")

    selection = int(input("\nEnter you selection:\t"))

    

#End