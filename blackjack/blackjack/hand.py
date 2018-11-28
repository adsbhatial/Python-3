class Hand():

    def __init__(self):
        self.cards = []
        self.points = 0
        self.aces = 0

    def add_card(self, game_card):
        self.cards.append(game_card)
        if game_card.letter == 1:
            self.aces = self.aces + 1

    def total_points(self):
        self.points = 0

        for card in self.cards:
            if card.letter == 1:
                continue
            else:
                self.points += card.value

        if ( ( self.aces * 11 ) + self.points ) <= 21:
            self.points = (self.aces * 11) + self.points
        elif ( self.points + self.aces + 10) <= 21:
            self.points = self.points + self.aces + 10
        else:
            self.points = self.points + self.aces
        
        return self.points
    
    def list_cards(self):
        cards_list = ""
        for card in self.cards:
            cards_list = cards_list + "\n" + str(card) + " value = " + str(card.value)

        cards_list = cards_list + "\n" + "Total points : " + str(self.total_points())

        return cards_list
        
    