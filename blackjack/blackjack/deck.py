'''
Script for a deck
'''
import random
from . import card

class Deck():
    '''
    Class for deck object
    '''

    def __init__(self):
        self.deck = []
        for val in range(1, 14):
            for typ in ["Spade", "Hearts", "Diamonds", "Clubs"]:
                if val < 11:
                    self.deck.append(card.Card(val, typ, val))
                elif val >= 11 and val <= 13:
                    self.deck.append(card.Card(val, typ, 10))
                else:
                    self.deck.append(card.Card(val, typ, 0))
        random.shuffle(self.deck)

    def remove_card(self):
        '''
        Removes a card from deck
        '''
        if len(self.deck) < 0:
            raise Exception
        else:
            return self.deck.pop()

    def __str__(self):
        str_deck = ""
        count = 1
        for card_element in self.deck:
            str_deck = str_deck + "\n" + str(count) + ") " + str(card_element)
            count += 1
        return str_deck

    def shuffle_deck(self):
        '''
        Shuffles the deck
        '''
        random.shuffle(self.deck)
