#Ryan Middle
#CSCI101
#Create Explore- BlackJack

import random
from time import sleep


print("Welcome to Blackjack! Here are some rules you need to know:"), sleep(1)
print("Player is dealt 2 cards face up, while the dealer has one card face up and one face down."), sleep(1)
print("Player is playing against the Dealer, attempting to collect cards that get the Player's hand as close to 21, without going over."), sleep(1)
print("Blackjack! is hit when the hand dealt to either the Player or Dealer is an Ace plus a 10 or face card."), sleep(1)
print("If Player gets dealt Blackjack!, the player immediately Wins. The House pays out 3:2. If only the Dealer gets Blackack! the player immediately loses."), sleep(1)
print("Players start with $1000, no table min or max bets."), sleep(1)
print("Dealer must hit on 16 and stay on soft 17"), sleep(1)
print("Insurance pays 2:1, max bet being 1/2 of original bet"), sleep(1)



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
    print('Dealer Hand:',dealerhand[0], '?'), sleep(1)
    print('Player Hand:',playerhand), sleep(1)
    print('Player Score:',score(playerhand)), sleep(1)
    print('Bet:', bet), sleep(1)
    print('Chips:', money), sleep(1)
def table2(playerhand,dealerhand,bet,money):
    print('Dealer Hand:',dealerhand), sleep(1)
    print('Dealer Score:', score(dealerhand)), sleep(1)
    print('Player Hand:',playerhand), sleep(1)
    print('Player Score:',score(playerhand)), sleep(1)
    print('Bet:', bet), sleep(1)
    print('Chips:', money), sleep(1)
                                            
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

deck=[] #init deck
for suit in suits:
    for card in cardval:
        deck.append((card,suit))
decks=deck #init single deck, along with one that is played with, decks initialized after each hand

def result(playerhand,dealerhand,bet,money):
    table2(playerhand,dealerhand,bet,money)
    while score(dealerhand) < 17:
        dealerhand=deal(dealerhand,1)
        table2(playerhand,dealerhand,bet,money)
    if score(playerhand) > 21:
        print('Bust! You lose')
    elif score(playerhand) < score(dealerhand) and score(dealerhand) < 22:
        print('Dealer Wins!')
    elif score(dealerhand) > 21:
        print('Dealer Bust! Hand Wins!')
        money += bet*2
    elif score(playerhand) > score(dealerhand):
        print('Hand Wins!')
        money += bet*2
    elif score(playerhand) == score(dealerhand):
        print('Push! Break Even.')
        money += bet
    print('Chips:', money)
    return float(money)
        



def playturn(playerhand,dealerhand,action,bet,money):
    table1(playerhand,dealerhand,bet,money)
    if action == 'Hit':
        playerhand=deal(playerhand,1)
        if score(playerhand) > 21:
            print('Bust!'), sleep(2)
            return result(playerhand,dealerhand,bet,money)
        elif score(playerhand) == 21:
            return result(playerhand,dealerhand,bet,money)
        else:
            table1(playerhand,dealerhand,bet,money)
            print('What would you like to do with your hand?')
            action=input('ACTION> ')
            return playturn(playerhand,dealerhand,action,bet,money)
        
    elif action == 'Stand':
        return result(playerhand,dealerhand,bet,money)

    elif action == 'DD':
        if bet > money:
            print('Error, insufficient funds to Double down. Please choose another action.')
            action=input('ACTION> ')
            return playturn(playerhand,dealerhand,action,bet,money)
        elif len(playerhand) > 2:
            print('Error: cannot double down after hitting. Please choose another action')
            action=input('ACTION> ')
            return playturn(playerhand,dealerhand,action,bet,money)
        else:
            money -= bet
            bet += bet
            playerhand=deal(playerhand,1)
            return result(playerhand,dealerhand,bet,money)
        
    else:
        print('Error: did not recognize input; please try again')
        action=input('ACTION> ')
        return playturn(playerhand,dealerhand,action,bet,money)
    
def SaveGame(file,money): #save progress function
    f=open(file,'w+')
    f.write(str(money))
    f.close()
def OpenGame(file): #open previous function
    f=open(file, 'r')
    money=f.readlines()
    f.close()
    return float(money[0])




#begin game
print('Would you like to open a previous game? (Y/N)?')
opengame=input('Y/N> ')
if opengame == 'Y':
    print('Enter the file location from which you saved your previous game')
    file=input('FILE> ')
    money=float(OpenGame(file))
else:
    money=float(1000)



turn=0
while turn == 0:
    print('--------------------------------------------------------------Shuffling Deck--------------------------------------------------------------')
    deck=decks
    playerhand=[]
    dealerhand=[]
    deal(playerhand,2)
    deal(dealerhand,2)
    x=0 #resets split fxn to determine money at end of turn
    #playerhand=[('10', 'Diamonds'), ('10', 'Hearts')] Used to test split parts of function

    print('Chips:',money)
    print('How much would you like to bet on this hand?')
    bet=float(input('BET> '))
    while bet > money:
        print('Error: insufficient funds to bet this big. Choose a more realistic number please')
        bet=float(input('BET> '))
    money -= bet
    insurance='N'
    
    table1(playerhand,dealerhand,bet,money)
    if score(playerhand) == 21:
        print('BlackJack! Pays 3:2'), sleep(2)
        money += bet*2.5
        turn=1
        
    else:
        if dealerhand[0][0] == 'A':
            ins = 'need'
            while ins == 'need':
                insurance=input('Would you like to buy insurance (Y/N)?> ')
                if insurance == 'Y':
                    insbet=float(input('How much would you like to place on insurance bet?'))
                    if insbet > money or insbet > bet*0.5:
                        print('Error: too much placed on insurance')
                    else:
                        ins='done'
                        money -= insbet
                elif insurance == 'N':
                    ins='done'
                else:
                    print('Error: did not recognize input. Please try again')
        if score(dealerhand) == 21:
            print('Dealer has BlackJack! Game Over')
            print(dealerhand)
            turn = 1
            if insurance == 'Y':
                print('Insurance pays 2:1'), sleep(2)
                money += insbet + insbet*2        
        elif score(dealerhand) != 21 and (dealerhand[0][0] == 'A' or cardval[dealerhand[0][0]] == 10):
            print('Dealer does NOT have BlackJack! Game On!'), sleep(1)
            
    while turn == 0:
        table1(playerhand,dealerhand,bet,money)
        print('What would you like to do with your hand (Hit, Stand, DD (Double Down), Split)?')
        action=input('ACTION> ')
        
        if action == 'Split':
            if bet > money or cardval[playerhand[0][0]] != cardval[playerhand[1][0]]:
                print('Error: cannot split, choose another action')
                action=input('ACTION> ')
                while action == 'Split':
                    print('Error: cannot split, choose another action')
                    action=input('ACTION> ')
                playturn(playerhand,dealerhand,action,bet,money)
            else:
                x=1
                money -= bet
                hand1=[]
                hand2=[]
                hand1.append(playerhand[0])
                hand2.append(playerhand[1])
                deal(hand1,1)
                deal(hand2,1)
                print('Hand 1:', hand1)
                print('Score Hand 1:', score(hand1))
                print('Hand 2:', hand2)
                print('Score Hand 2:', score(hand2))
                print('What would you like to do with Hand 1 (DO NOT SPLIT OR DD, can only do these once per turn!)?')
                action=input('ACTION> ')
                while action == 'Split' or action == 'DD':
                    print('Error: cannot make this selection; please try again.')
                    print('What would you like to do with Hand 1? (DO NOT SPLIT OR DD, can only do these once per turn!)?')
                    action=input('ACTION> ')
                while action == 'Hit' and score(hand1) < 21:
                    hand1=deal(hand1,1)
                    print('Hand1:',hand1)
                    print('Score Hand1',score(hand1))
                    if score(hand1) < 21:
                        print('What would you like to do with Hand 1(DO NOT SPLIT OR DD, can only do these once per turn!)?')
                        action=input('ACTION> ')
                print('Hand1:', hand1)
                print('Score Hand1', score(hand1))
                print('Hand2:', hand2)
                print('Score Hand2:', score(hand2))
                print('What would you like to do with Hand 2(DO NOT SPLIT OR DD, can only do these once per turn!)?')
                action=input('ACTION> ')
                while action == 'Split' or action == 'DD':
                    print('Error: cannot make this selection; please try again.')
                    print('What would you like to do with Hand 2? (DO NOT SPLIT OR DD, can only do these once per turn!)?')
                    action=input('ACTION> ')
                while action == 'Hit' and score(hand2) < 21:
                    hand1=deal(hand2,1)
                    print('Hand2:',hand2)
                    print('Score Hand2',score(hand2))
                    if score(hand2) < 21:
                        print('What would you like to do with Hand 1(DO NOT SPLIT OR DD, can only do these once per turn!)?')
                        action=input('ACTION> ')
                result(hand1,dealerhand,bet,money), result(hand2,dealerhand,bet,money)
            

                        
            
        else:
            playturn(playerhand,dealerhand,action,bet,money)
        if action == 'DD':
            money=result(playerhand,dealerhand,bet*2,money-bet)
        elif x == 1:
            money=result(hand1,dealerhand,bet,money)
            money=result(hand2,dealerhand,bet,money)
        else:
            money=result(playerhand,dealerhand,bet,money)
            
        turn=1
    while turn == 1:
        print('Hand Over! Play Again (Y/N)?')
        playagain=input('Y/N> ')
        if playagain == 'Y' and money != 0:
            turn=0
        elif money <= 0 and playagain == 'Y':
            print('Bankrupt; getting loan from bank......')
            money += 1000
            turn=0
        else:
            print('Would you like to save your progress (Y/N)?')
            savegame=input('Y/N> ')
            if savegame == 'Y' and money !=0:
                print('Please input the file location for your progress to be saved')
                file=input('FILE LOCATION> ')
                SaveGame(file,money)
                print('Thanks for Playing!')
            elif savegame == 'Y' and money == 0:
                print('Error, cannot save progress because you are bankrupt. Thanks for Playing!')
            else:
                print('Thanks for Playing')
                
            break
            break
            break
            break

                


























