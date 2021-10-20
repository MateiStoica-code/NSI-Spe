from random import *
card_families = ["of Spades","of Hearts","of Diamonds","of Clubs"]
card_values = ['Ace', '2','3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']



def build_deck() :
    deck = []
    for i in range(len(card_families)) :
        for j in range(len(card_values)) :
            deck.append ((card_values[j] , card_families[i]))
    return(deck)

def shuffle_deck() :
    deck = build_deck()
    shuffle(deck)
    return(deck)

def deal_cards(deck, n, deal_method):
    if n == 0 :
        return("There cannot be a game with no players...it's not a game then :|")

    if len(deck) == 0 :
        return("You can't play cards without a deck...Here's 5€, go buy a card deck.")

    if deal_method !=1 and deal_method !=2 :
        return("You need to select a valid dealing method. I have implemented two methods : 1 is to deal all of a players' cards at once and 2 is to deal to each player one card each time, circularily")

    len_slice = len(deck)//n
    discard_cards = len(deck)%n
    players = []
    discard_pile = []


    #To deal all of a player's cards at once, method == 1
    if deal_method == 1 :
        for i in range(n) :
            slice_start = len_slice*i
            slice_stop = (len_slice-1)*(i+1)
            players.append(deck[slice_start:slice_stop])


    #to deal cards one by one to each player
    if deal_method == 2 :
        for i in range(n) :
            slice_start = i
            slice_stop = len(deck)-discard_cards
            players.append(deck[slice_start:slice_stop:n])
            print(len(players))

    discard_pile.append(deck[(len_slice*n):])


    return("players' cards =",players,"discard pile =", discard_pile)
