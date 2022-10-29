import random
# deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "K", "Q", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "K", "Q", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "K", "Q", 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "K", "Q"]
player_hand = []
dealer_hand = []

sum_player = 0
sum_dealer = 0
dealt_card = 0

def player_deal():
    global sum_player
    global sum_dealer 
    global dealt_card 
    dealt_card = deck.pop(random.randint(0, len(deck)-1))
    player_hand.append(dealt_card)
    if dealt_card in range(2, 11):
        sum_player += dealt_card
    elif dealt_card in ["J", "K", "Q"]:
        sum_player += 10
    else:
        if sum_player > 10:
            sum_player += 1
        else:
            sum_player += 11
    print("Player hand: " + str(player_hand))
    print("Player sum: " + str(sum_player))


def dealer_deal():
    global sum_player
    global sum_dealer 
    global dealt_card 
    dealt_card = deck.pop(random.randint(0, len(deck)-1))
    dealer_hand.append(dealt_card)
    if dealt_card in range(2, 11):
        sum_dealer += dealt_card
    elif dealt_card in ["J", "K", "Q"]:
        sum_dealer += 10
    else:
        if sum_dealer > 10:
            sum_dealer += 1
        else:
            sum_dealer += 11
    
    if len(dealer_hand) == 2:
        print("Dealer hand: " + str(dealer_hand[0]) + " X")
    else:
        print("Dealer hand: " + str(dealer_hand))
        print("Dealer sum: " + str(sum_dealer))

def return_sum():
    return "Player: " + str(sum_player) + " Dealer: " + str(sum_dealer)

while True:
    player_deal()
    dealer_deal()
    player_deal()
    dealer_deal()
    if sum_player == 21:
        print("Blackjack, player won!")
        break
    answer = input("Hit or stay?")

    while answer == "hit":
        player_deal()
        if sum_player > 21:
            print("BUST! Player lost!")
            break
        answer = input("Hit or stay?")
        if answer == "stay":
            print("Dealer hand: " + str(dealer_hand))
            print("Dealer sum: " + str(sum_dealer))
            continue
    if sum_player>21:
        break

    if sum_dealer <= 16:
	    dealer_deal()
	    if sum_dealer > 21:
	        print("BUST! Player won!" + "Player: " + str(sum_player) + " Dealer: " + str(sum_dealer))
	        break

    if sum_player > sum_dealer and sum_player <= 21:
	    print("Player won!" + return_sum())
    elif sum_player == sum_dealer:
        print("TIE!")
    else:
	    print("Dealer won!" + "Player: " + return_sum())
    break
