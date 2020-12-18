############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
from math import fsum
from art import logo
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#function to get initial hand#
def initialHand():
    firstCard = random.choice(cards)
    secondCard = random.choice(cards)
    return [firstCard, secondCard]
    

#function to draw card and calculate#
def hitMe():
    return random.choice(cards)


#This converts 11 to 1 if user/computer over 21#
def aceButOver(hand):
      total = int(fsum(hand))
            
      lastOne = len(hand) - 1

      if hand[lastOne] == 11 and total > 21:
          hand[lastOne] = 1
          return hand

      else:
          return hand  


def getFinalHand(hand, whoIsIt):
    anotherCard = True

    while anotherCard:
        
        #if it's the user
        if whoIsIt == 1:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                hand.append(hitMe())
                              
                hand = aceButOver(hand)
                total = int(fsum(hand))

                print(f"You Hold: {hand} for a total of: {total}")
            
                if total > 21:
                    return 0
                
                elif total == 21:
                    anotherCard = False
                    
            else:
                anotherCard = False
               
        elif whoIsIt == 0:
            hand.append(hitMe())
            hand = aceButOver(hand)
            total = int(fsum(hand))
       
            if total > 21:
                print(f"Computer's final hand: {hand}")
                return 0

            elif total >= 17:
                print(f"Computer's final hand: {hand}")
                anotherCard = False        

            else:
                print(f"Dealer Draw Again: {hand}")
    
    print()
    return int(fsum(hand)) 
      
       


def theWinnerIs(dealHand, usrHand):
    if dealHand > usrHand:
        print("You Lose :(")
    
    elif dealerHand < finalHand:
        print("You Win!")

    elif dealerHand == finalHand:
        print("It's a Draw!")

    else:
        print("Unable to compute results, try again")
        


#Program Starts Here#
keepPlaying = True

while keepPlaying:
    os.system("clear")
    print(logo)     
    userHand = initialHand()
    dealerHand = [hitMe()]

    print(f"You cards: {userHand}")
    print(f"Computer's first card: {dealerHand}")
    
    if int(fsum(userHand)) == 21:
        print("You win with a Black Jack!")

    else:
        finalHand = getFinalHand(userHand, 1)

        if finalHand == 0:
            print("You Bust, Game Over!")

        else:
            dealerHand = getFinalHand(dealerHand, 0)

            if dealerHand == 0:
                print("Dealer Busts, You Win!")
        
            else: 
                theWinnerIs(dealerHand, finalHand)

    print()
    keepOn = input("Do you want to play another game of BlackJack? Type 'y' or 'n'")
    if keepOn == 'n':
        keepPlaying = False
    