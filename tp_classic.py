


#patterns

#have to check for chatti

"""
twice 1
coloured not round done 2
round not coloured done 3
coloured round done 4
thrice 5
"""



def is_coloured(num_card, type_card):
    if(len(list(set(type_card)))==1):
        return True
    else:
        return False

def is_round(num_card, type_card):
    num_card.sort()
    if(num_card[1] == (num_card[2] + num_card[0])/2):
        return True
    else:
        return False


def is_coloured_is_round(num_card, type_card):
    return [is_coloured(num_card, type_card), is_round(num_card, type_card)]

def is_twice(num_card, type_card):
    if(len(list(set(num_card)))==2):
        return True
    else:
        return False

def is_thrice(num_card, type_card):
    if(len(list(set(num_card)))==1):
        return True
    else:
        return False



def card_pattern_checker(user_cards):
    res = 0
    num_card = [i[0] for i in user_cards]
    type_card = [i[1] for i in user_cards]
    if(is_twice(num_card, type_card)):
        res+=1
        if(num_card.count(num_card[0])==2):
            twice_num_card = num_card[0]
            if (num_card.count(num_card[1]) == 1):
                single_num_card = num_card[1]
            else:
                single_num_card = num_card[2]
        else:
            twice_num_card = num_card[1]
            single_num_card = num_card[0]
        res+=twice_num_card/100 + single_num_card/10000
        return res
    if(is_coloured_is_round(num_card, type_card) == [True, False]):
        res+=2
        num_card.sort(reverse=True)
        biggest_card = num_card[0]
        second_card = num_card[1]
        smallest_card = num_card[2]
        if(biggest_card==13 and second_card==2 and smallest_card==1):
            #rangi chatti condition
            res+=0.2 #still bigger than 0.1313
        else:
            res+=biggest_card/100 + second_card/10000 + smallest_card/1000000
        return res
    if(is_coloured_is_round(num_card, type_card) == [False, True]):
        num_card.sort()
        res+=3
        biggest_card = num_card[-1]
        res+=biggest_card/100
        return res
    if(is_coloured_is_round(num_card, type_card) == [True, True]):
        num_card.sort()
        res+=4
        biggest_card = num_card[-1]
        res+=biggest_card/100
        return res
    elif(is_thrice(num_card, type_card)):
        res+=5
        only_card_num = list(set(num_card))[0]
        res+=only_card_num/100
        return res
    else:
        num_card.sort()
        if(num_card[-1]==13 and num_card[0]==1 and num_card[1]==2):
            #chatti condition provided chatti is better than first
            res+=3.2 #0.20 is bigger than max 0.1313`
        else:
            biggest_card = num_card[-1]
            second_card = num_card[1]
            smallest_card = num_card[0]
            res+=biggest_card/100 + second_card/10000 + smallest_card/1000000

    return res




#print(card_pattern_checker([[2, 'Heart'], [2, 'Spade'], [9, 'Spade']]))
#print(card_pattern_checker([[9, 'Heart'], [2, 'Spade'], [9, 'Spade']]))

#print(card_pattern_checker([[6, 'Heart'], [2, 'Heart'], [9, 'Heart']]))
#print(card_pattern_checker([[6, 'Spade'], [2, 'Spade'], [11, 'Spade']]))












