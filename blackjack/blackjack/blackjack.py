'''
A simple script for text based blackjack
'''
from . import deck
from . import player

class Blackjack():
    '''
    Class to create basic blackjack object
    '''
    def __init__(self, bet, dealer, gambler):
        self.bet = bet
        self.game_deck = deck.Deck()
        self.game_deck.shuffle_deck()
        self.gambler = gambler
        self.dealer = dealer

    def hit(self, game_player):
        '''
        Method to emulate hit action in blackjack
        Returns a tupple
        '''
        removed_card = self.game_deck.remove_card()
        if self.gambler == game_player:
            self.gambler.add_card(removed_card)
        elif self.dealer == game_player:
            self.dealer.add_card(removed_card)
        else:
            raise Exception

        if game_player.points() > 21:
            return (False, str(removed_card), game_player.points())

        return (True, str(removed_card), game_player.points())

    def start_turn(self, dealer, game_player):
        '''
        Returns True if player busts
        Returns False if player survives
        '''
        if dealer:
            while True and self.hit(game_player)[0]:
                if game_player.points() >= 17:
                    return False
            return True
        elif not dealer:
            while True:
                print("Current Cards : ", game_player.hand_cards.list_cards())
                print("\nDo you want to hit or pass?")
                choice = input("Press h for hit, any other key for pass: ")
                if choice[0] == "h":
                    if not self.hit(game_player)[0]:
                        print("Current Cards : ", game_player.hand_cards.list_cards())
                        return True
                else:
                    return False

        raise Exception

def correct_value(message, limit):
    '''
    Function takes user input till valid value is given
    '''
    while True:
        try:
            print(message)
            inp = int(input())
            if limit > 0 and inp > limit:
                raise ValueError
        except ValueError:
            print("Please enter correct value!")
        else:
            return inp
