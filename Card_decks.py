from random import *
card_families = ["of Spades","of Hearts","of Diamonds","of Clubs"]
card_values = ['Ace', '2','3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']



def build_deck() :
    deck = []
    whatever = ()
    for i in range(len(card_families)) :
        for j in range(len(card_values)) :
            deck.append ((card_values[j] , card_families[i]))
    return(deck)

def shuffle_deck() :
    deck = build_deck()
    shuffle(deck)
    return(deck)

def deal_cards(deck, n):

    len_slice = len(deck)//n
    discard = len(deck)%n
    players = []
    pot = []


    #To deal all of a player's cards at once

    for i in range(n) :
        slice_start = len_slice*i
        slice_stop = (len_slice-1)*(i+1)
        players.append(deck[slice_start:slice_stop])


    #to deal cards one by one to each player

    for i in range(n) :
        slice_start = i
        slice_stop = len(deck)-discard
        players.append(deck[slice_start:slice_stop:n])
    pot.append(deck[(len_slice*n):])
    return("players =",players,"pot =", pot)



numbers = [i for i in range(51)]
print(numbers)
slic = numbers[0::5]
print(slic)
slic = numbers[1::5]
print(slic)