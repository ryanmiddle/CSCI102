#Ryan Middle
#CSCI101
#Create Explore- BlackJack

import random
from time import sleep
#initializing values for cards
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

def table1(playerhand,dealerhand,bet,money):
    print('Your Hand:',playerhand)
    print('Your Score:', score(playerhand))
    print('Bet:', bet, 'Chips:', money)
    print('Dealer Hand:', dealerhand[0],'?')
def table2(playerhand,dealerhand,bet,money):
    print('Your Hand:',playerhand)
    print('Your Score:', score(playerhand))
    print('Bet:', bet, 'Chips:', money)
    print('Dealer Hand:', dealerhand)
    print('Dealer Score:', score(dealerhand))



                                            
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
        if g == 'A':
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

def playturn(hand,action,turn,bet=0,money=0):
    if action == 'Hit':
        deal(hand, 1)
        print('Hand:',hand),
        print('Score:',score(hand)),
        if bet != 0:
            print('Bet',bet, 'Chips:',money),
        if score(hand) > 21 and turn != 'Dealer':
            print('Bust! Dealers turn')
            turn='Dealer'
        return hand, turn, bet, money
            
    elif action == 'Stand':
        turn='Dealer'
        print('Hand:',hand)
        print('Score:',score(hand))
        if bet != 0:
            print('Bet',bet, 'Chips:',money)
        return hand, turn, bet, money
    
    elif action == 'DD':
        if bet > money:
            print('Error: insufficient funds to double down, please choose another option')
        else:
            money -= bet
            bet += bet
            deal(hand,1)
            if score(hand) > 21:
                print('Bust! Dealers turn')
            turn='Dealer'
            print('Hand:',hand)
            print('Score:',score(hand))
            if bet != 0:
                print('Bet',bet, 'Chips:',money)
        return hand, turn, bet, money
            
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
            money = money - bet
            bet += bet
            print('Hand 1:', hand1)
            print('Hand 2:', hand2)
            while turn == 'hand1':
                action=input('What would you like to do with Hand 1? (Hit, Stand, DD?')
                if action == 'Split':
                    print('Error: can only split once, please choose another option')
                else:
                    playturn(hand1,action,turn,bet,money)
                    if action == 'Stand':
                        turn='hand2'
                    elif score(hand1) > 21:
                        print('Bust! now play for hand 2')
                        turn='hand2'
            while turn == 'hand2':
                action=input('What would you like to do with Hand 2? (Hit, Stand, DD?')
                playturn(hand2,action,turn,bet,money)
            turn='Dealer'
            print('Hand 1:',hand1)
            print('Score 1:',score(hand1))
            print('Hand 2:',hand2)
            print('Score 2:',score(hand2))
            print('Bet',bet)
            print('Chips:',money)
            return hand1, hand2, turn, bet, money
    

def SaveGame(file,money):
    f=open(file,'w+')
    f.write(str(money))
    f.close()
def OpenGame(file):
    f=open(file, 'r')
    money=f.readlines()
    f.close()
    return float(money[0])

playerhand=[]
dealerhand=[]
deal(playerhand,2)
deal(dealerhand,2)
turn=0

game = 'Y'
while game == 'Y':
    turn='Player'
    print('Would you like to load an existing game(Y/N)?')
    load=input('LOAD GAME?> ')
    if load == 'Y':
        print('Please enter the file path to where you saved your progress')
        file=input('FILE LOCATION> ')
        money=OpenGame(file)
    else:
        money=float(1000)
    print('How much would you like to bet on this game?')
    bet=float(input('BET> '))
    money -= bet
    playerhand=[]
    dealerhand=[]
    deal(playerhand,2)
    deal(dealerhand,2)
    table1(playerhand,dealerhand,bet,money)
    
    if dealerhand[0][0] == 'A':
        ins='need'
        #checking for insurance
        while  ins == 'need':
            insurance=input("Would you like insurance? (Y/N)")
            if insurance == 'Y':
                insurancebet=input("How much would you like to place on insurance?")
                money -= insurancebet
                if insurancebet > money or insurancebet > bet*0.5:
                    print("Error: too much money placed on insurance")
                else:
                    ins='done'
            else:
                ins='done'
            if score(dealerhand) == 21:
                print("Dealer has BlackJack!")
                print(dealerhand)
                turn='over'
                if insurance == 'Y':
                    money += insurancebet + insurancebet*2
    else:
        ins='done'
        print("Dealer Does NOT have BlackJack!")
    hands=1
    while turn == 'Player':
        table1(playerhand,dealerhand,bet,money)
        print('What would you like to do with your hand (Hit, Stand, DD (Double Down), Split?')
        action=input('ACTION> ')
        if action == 'Split':
            hands=2
        playturn(playerhand,action,turn,bet,money)
    while turn == 'Dealer':
        while score(dealerhand) < 17:
            table2(playerhand,dealerhand,bet,money)
            deal(dealerhand,1)
        if score(dealerhand) > 17:
            turn='Result'
        if hands == 2:
            if score(hand1) < 22 and score(hand1) > score(dealerhand):
                print('Hand 1 Wins!')
            else:
                print('Hand 2 Loses!')
                money += bet/2
            if score(hand2) < 22 and score(hand2) > score(dealerhand):
                print('Hand 2 Wins!')
            else:
                print('Hand 2 Loses!')
                money += bet/2
        if score(playerhand) > score(dealerhand) and score(playerhand) < 21:
            print('You Win! Play again (Y/N)')
            money += bet*2
            game=input('NEW GAME> ')
        elif score(playerhand) < 21 and score(dealerhand) > score(playerhand):
            print('You Lose! Play again (Y/N)?')
            game=input('NEW GAME> ')
        if game == 'N':
            print('Would You like to save your progress (Y/N)')
            save=input('SAVE GAME> ')
        if save == 'Y':
            print('Please type a file location to save your progress')
            file=input('FILE> ')
            SaveGame(file,money)
                
                













  
