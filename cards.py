import random

card_types = [i+1 for i in range(13)] #1 is 2, 2 is 3 and so on till 13 is ace
divisions = ['Spade', 'Club', 'Diamond', 'Heart']

deck = [[i,j] for i in card_types for j in divisions]

joker_bool = False
if(joker_bool==True):
    deck+=[100, 'All'] #will work with this later

def deck_shuffler():
    random.shuffle(deck)
    return None

def card_distribute(no_of_players):
    table = [[] for i in range(no_of_players)]
    deck_shuffler()
    #print(deck[:3*no_of_players])
    for i in range(no_of_players):
        tempList = [no_of_players*j+i for j in range(3)]
        for j in tempList:
            table[i].append(deck[j])
            
    #print(table)   
    return table

#print(card_distribute(3))







