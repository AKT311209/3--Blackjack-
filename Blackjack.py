""" This is the module imitating the Blackjack game """
import random
import os
# Cards
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
LOOP = 0
# Objects


class Cards():
    """ This is the  class for cards"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck():
    """ This is the class for a new deck """

    def __init__(self):
        self.all_cards = []
        for cardsuit in suits:
            for cardrank in ranks:
                new_cards = Cards(cardsuit, cardrank)
                self.all_cards.append(new_cards)
        self.shuffle()

    def draw(self):
        """ This method is for drawing cards """
        return self.all_cards.pop(0)

    def shuffle(self):
        """ This method is for shuffling the starting Deck """
        random.shuffle(self.all_cards)


class Player():
    """ This is the class for the player hand"""

    def __init__(self, name, money):
        self.inhand = []
        self.value = 0
        self.money = money
        self.name = name
        self.ace = []

    def drawcard(self, card):
        """ This is the method for drawing card or HIT """
        self.inhand.append(card)
        if card.value == 11:
            self.ace.append(card)
        self.value += card.value
        self.valuecalc()

    def __str__(self) -> str:
        return f'Player {self.name} with value {self.value}, with {len(self.ace)} ACES'

    def valuecalc(self):
        """ This is for the recalculation of hand value (Ace) """
        for _ in self.ace:
            if self.value > 21:
                self.value -= 10
                self.ace.pop(0)

    def checkburst(self):
        """ This method is for checking whether a player has 'burst' """
        if self.value > 21:
            return True
        else:
            return False

    def bet(self):
        while True:
            print(f'Your current money: {self.money}')
            bet_money = input('Please place your bet: ')
            if bet_money.isdigit() is False:
                print('Please enter a valid number!')
            elif int(bet_money) > self.money:
                print('You can not bet more than what you have!')
            else:
                bet_money = int(bet_money)
                self.money -= bet_money
                return bet_money

    def win(self, money):
        self.money += money

    def check_lose(self):
        if self.money <= 0:
            return True
        else:
            return False

    def clear_card(self):
        self.inhand.clear()
        self.value = 0
        self.ace = []


class Dealer(Player):
    """ This class is for computer dealer """

    def __init__(self, dealer_money):
        super().__init__('Dealer', dealer_money)

    def reveal_cards(self):
        return self.inhand[-1]

    def lose(self, money):
        self.money -= money
        self.check_lose()

# Function


def clear_screen():
    try:
        os.system('cls')
    except:
        os.system('clear')


def player_drawing():
    print('Dealer cards: ')
    print('FACEDOWN')
    print(dealer.reveal_cards())
    print('-------------------------------------------------------')
    while True:
        print('Your cards: ')
        for card in player.inhand:
            print(card)
        choice = input('DO YOU WANT TO HIT, Y or N?: ')
        if choice == 'N':
            return 'Ok'
        elif choice == 'Y':
            player.drawcard(card_pile.draw())
            if player.checkburst() is True:
                return 'Burst'
            else:
                pass
        else:
            print('Please enter N or Y valid.')


def dealer_drawing():
    while True:
        if dealer.value < 11:
            dealer.drawcard(card_pile.draw())
            if dealer.checkburst() is True:
                return 'Burst'
            else:
                pass
        elif 11 <= dealer.value < 14:
            if random.choice([0, 1, 1, 1]) == 1:
                dealer.drawcard(card_pile.draw())
                if dealer.checkburst() is True:
                    return 'Burst'
                else:
                    pass
            else:
                return 'Ok'
        elif 14 <= dealer.value < 16:
            if random.choice([0, 1]) == 1:
                dealer.drawcard(card_pile.draw())
                if dealer.checkburst() is True:
                    return 'Burst'
                else:
                    pass
            else:
                return 'Ok'
        elif 16 <= dealer.value < 18:
            if random.choice([0, 1, 0, 0]) == 1:
                dealer.drawcard(card_pile.draw())
                if dealer.checkburst() is True:
                    return 'Burst'
                else:
                    pass
            else:
                return 'Ok'
        elif 18 <= dealer.value < 20:
            if random.choice([0, 1, 0, 0, 0]) == 1:
                dealer.drawcard(card_pile.draw())
                if dealer.checkburst() is True:
                    return 'Burst'
                else:
                    pass
            else:
                return 'Ok'
        else:
            if dealer.checkburst() is True:
                return 'Burst'
            else:
                return 'Ok'


# MAIN SCRIPT START HERE
while True:
    while True:
        player_asked_money = input(
            'Please enter the value of money you want to start with: ')
        dealer_asked_money = input(
            'Please enter the value of money you want the dealer to start with: ')
        if player_asked_money.isdigit() is True and dealer_asked_money.isdigit() is True:
            player = Player('player', int(player_asked_money))
            dealer = Dealer(int(dealer_asked_money))
            card_pile = Deck()
            print('_____________________________________________________________________________________')
            break
        print('Please enter a number!')

    while True:
        LOOP += 1
        card_pile = Deck()
        bet_ammount = player.bet()
        print('------------------------------------------------------------------------')
        player.clear_card()
        dealer.clear_card()
        player.drawcard(card_pile.draw())
        player.drawcard(card_pile.draw())
        dealer.drawcard(card_pile.draw())
        dealer.drawcard(card_pile.draw())
        if player_drawing() == 'Burst': 
            print('*********************************************')
            print('Your cards: ')
            for pcard in player.inhand:
                print(pcard)
            print('*********************************************')    # if both burst then player lose.
            print('You BURST!')
            dealer.win(bet_ammount)
            print('You have lost this round.')
        elif dealer_drawing() == 'Burst':
            print('*********************************************')
            print("Dealer's cards: ")
            for dcard in dealer.inhand:
                print(dcard)
            print('*********************************************')
            print('Dealer BURST!')
            dealer.lose(bet_ammount)
            player.win(2*bet_ammount)
            print('You have won this round.')
        else:
            print('*********************************************')
            print('Your cards: ')
            for pcard in player.inhand:
                print(pcard)
            print('*********************************************')
            print("Dealer's cards: ")
            for dcard in dealer.inhand:
                print(dcard)
            print('*********************************************')
            if (21 - player.value) > (21 - dealer.value):   # Player lose
                dealer.win(bet_ammount)
                print('You have lost this round.')
            elif (21 - player.value) < (21 - dealer.value):  # Player win
                dealer.lose(bet_ammount)
                player.win(2*bet_ammount)
                print('You have won this round.')
            else:
                print('You have drawn with the dealer.')
                player.win(bet_ammount)
        if player.check_lose() is True:
            print('You have LOST the game because you ran out of money')
            break
        elif dealer.check_lose() is True:
            print('You have WON the game because Dealer ran out of money.')
            break
        else:
            pass
        print(f'Your money: {player.money}\nDealer money: {dealer.money}')
        print('......................................................................................................')
        print('New round')
    print(f'You have played {LOOP} rounds.')
    exit_choice = input(
        "Input 'new' if you want to play new game. Otherwise, enter anything to exit: ")
    if exit_choice == 'new':
        clear_screen()
        print('NEW GAME')
    else:
        break
