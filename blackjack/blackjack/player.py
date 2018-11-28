'''
Player object
'''

from . import card
from . import hand
class Player():

    def __init__(self, money):
        self.money = money
        self.hand_cards = hand.Hand()

    def add_card(self, card):
        self.hand_cards.add_card(card)

    def points(self):
        return self.hand_cards.total_points()

    def add_money(self, money):
        self.money = self.money + money

    def remove_money(self, money):
        if self.money - money < 0:
            return False
        else:
            self.money = self.money - money
            return True

    def get_money(self):
        return self.money
    
    def reset_hand(self):
        self.hand_cards = hand.Hand()
