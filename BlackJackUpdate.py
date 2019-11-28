#Ryan Middle
#CSCI101
#Create Explore- BlackJack

import random
cardval = {
'A': 11,
'2': 2,
'3':3,
'4':4,
'5':5,
'6':6,
'7':7,
'8':8,
'9':9,
'10':10,
'J':10,
'K':10
}
suits=['Spades', 'Hearts', 'Clubs', 'Diamonds']

def score(hand):
    '''
    this function will be used to calculate the scocre of cards in hand during play
    input: 'hand' containing cards
    output: score of list
    '''
    points=0
    a=0
    for card in hand:
        g=card[0]
        points += cardval[g]
        if card == 'A':
            a += 1 #counts number of aces in hand
        if a != 0 and points > 21:
            points -= 10 #turns value of ace to 1
            a -= 1 #reduces number of aces seen by 1
    return points

def deal(hand, a):
    for i in range(a):
        cards=random.randint(0,len(deck)-1)
        hand.append(deck[cards])
        deck.pop(cards)
    return hand

deck=[]
for suit in suits:
    for card in cardval:
        deck.append((card,suit))

def playturn(hand,action,bet=0, money=0):
    if action == 'Hit':
        deal(hand, 1)
        print('Hand:',hand),
        print('Score:',score(hand)),
        print('Bet',bet),
        print('Chips:',money)
        if score(hand) > 21:
            print('Bust! Dealers turn')
            turn='Dealer'
            
    elif action == 'Stand':
        turn='Dealer'
        print('Hand:',hand)
        print('Score:',score(hand))
        print('Bet',bet, 'Chips:',money)
        
    elif action == 'DD':
        if bet > money:
            print('Error: insufficient funds to double down, please choose another option')
        else:
            money -= bet
            bet += bet
            deal(hand,1)
            turn='Dealer'
            print('Hand:',hand)
            print('Score:',score(hand))
            print('Bet',bet)
            print('Chips:',money)
            
    elif action == 'Split':
        if bet > money:
            print('Error: insufficient funds to split, please choose another option')
        elif cardval[hand[0][0]] != cardval[hand[1][0]]:
            print('Error, cannot split different value cards, please choose another option')
        else:
            hand1=[]
            hand2=[]
            hand1.append(hand[0])
            deal(hand1,1)
            hand2.append(hand[1])
            deal(hand2,1)
            turn='hand1'
            money -= bet
            bet += bet
            print('Hand 1:', hand1)
            print('Hand 2:', hand2)
            while turn == 'hand1':
                action=input('What would you like to do with Hand 1? (Hit, Stand, DD?')
                if action == 'Split':
                    print('Error: can only split once, please choose another option')
                else:
                    playturn(hand1,action,bet,money)
                    if action == 'Stand':
                        turn='hand2'
                    elif score(hand1) > 21:
                        print('Bust! now play for hand 2')
                        turn='hand2'
            while turn == 'hand2':
                action=input('What would you like to do with Hand 2? (Hit, Stand, DD?')
                playturn(hand2,action)
            turn='Dealer'
            print('Hand 1:',hand1)
            print('Score 1:',score(hand1))
            print('Hand 2:',hand2)
            print('Score 2:',score(hand2))
            print('Bet',bet)
            print('Chips:',money)
    

def SaveGame(file,money):
    f=open(file,'w+')
    f.write(str(money))
    f.close()
def OpenGame(file):
    f=open(file, 'r')
    money=f.readlines()
    f.close()
    return int(money[0])

playerhand=[]
dealerhand=[]
deal(playerhand,2)
deal(dealerhand,2)
turn=0
if score(dealerhand) < 17:
    playturn(dealerhand,'Hit')

    
 
