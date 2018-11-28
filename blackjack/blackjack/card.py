class Card():
    '''
    Class for card object
    '''

    def __init__(self, letter, suit, value):
        self.letter = letter
        self.suit = suit
        self.value = value
        if letter == 1:
            self.name = f"Ace of {self.suit}"
        elif letter == 11:
            self.name = f"Jack of {self.suit}"
        elif letter == 12:
            self.name = f"Queen of {self.suit}"
        elif letter == 13:
            self.name = f"King of {self.suit}"
        else:
            self.name = f"{self.letter} of {self.suit}"

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return self.name
