from cards import *
from tp_classic import *
import time

game_types = ['Teen Patti Classic Single Winner', 'Teen Patti Classic'] #add game types in here

#shuffling once..
deck_shuffler()

def table_budget():
    print('Enter table entry value')
    val = int(input()) #change this later to float for allowing decimal plays
    if(val>0):
        return val
    else:
        print('Negative value not possible...reenter')
        return table_budget()

def no_of_players_input():
    print('Select No. of Players')
    no = int(input())
    if(no<=17 and no>0):
        return no
    else:
        print('Wrong input..{} players cant play!'.format(no))
        return no_of_players_input()
        
def player_info_input(ind, fee):
    print('Enter name of Player {}'.format(ind+1))
    name = str(input())
    print('Enter balance of Player {}'.format(ind+1))
    balance = int(input()) #change this in future to allow decimal balances and transactions
    if(balance>fee):
        return [name, balance]
    else:
        print('Negative or less than fee balance not allowed. Enter info again')
        return player_info_input(ind, fee)
        

if __name__ == '__main__':
    print('Starting table...')
    #table entry value
    fee = table_budget()
    #number of players
    num = no_of_players_input()
    #player info
    players_info = [] #inside each list in this list, 1st element has name and second has balance(dynamic)
    lost_players =[]
    for i in range(num):
        players_info.append(player_info_input(i, fee))
    player_names = [i[0] for i in players_info]
    while(len(player_names) != len(list(set(player_names)))):
        print('Players with same name found...enter info again')
        for i in range(num):
            players_info.append(player_info_input(i, fee))


    #game_type
    print('Choose game type')
    for i in range(len(game_types)):
        print('For playing {}, enter {}'.format(game_types[i], i))
    type = -1 #random initialisation
    while(type==-1 or type>len(game_types)):
        type = int(input())#add some line in here for recurring

    type_of_game = game_types[type]
    print(fee, num, players_info, type_of_game)

    #operating game type
    print('Starting Game...')
    ini_time = time.time()
    if(type_of_game=='Teen Patti Classic'):
        print('How much maximum rounds do you need to play?')
        max_rounds = int(input())
        for i in range(max_rounds):
            if(num>1):
                print('Game {} started'.format(i + 1))
                for j in range(num):
                    players_info[j][1] -= fee  # fee received
                print('Shuffling Cards...')
                players_cards = card_distribute(num)
                for j in range(num):
                    print('Player {} has cards: {}'.format(players_info[j][0], players_cards[j]))
                players_scores = [card_pattern_checker(k) for k in players_cards]
                winner_index = players_scores.index(max(players_scores))
                players_info[winner_index][1] += num * fee
                print('Player {} Won!'.format(players_info[winner_index][0]))
                for j in players_info:
                    print("Player {} has {} balance after this game".format(j[0], j[1]))
                for j in players_info:
                    if (j[1] < fee):
                        lost_players.append(j)
                        players_info.remove(j)
                        num -= 1
            else:
                print('Before completing {} rounds, all other players except {} have lost. Congratulations {}'.format(max_rounds, players_info[0][0], players_info[0][0]))
                print('Final Standings are:')
                print('{}:Rs{}'.format(players_info[0][0], players_info[0][1]))
                for j in lost_players:
                    print('{}:Rs{}'.format(j[0], j[1]))
                quit() #need to exit out of code##########################################################

        print('{} rounds are finished'.format(max_rounds))
        print('Final Standings are:')
        for j in players_info:
            print('{}:Rs{}'.format(j[0], j[1]))
        for j in lost_players:
            print('{}:Rs{} #Lost'.format(j[0], j[1]))
        print('Time elapsed: {}s'.format(round(time.time() - ini_time, 2)))