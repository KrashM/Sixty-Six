class Cards:
    def __init__(self):
        self.suits = ['♠', '♡', '♢', '♣']
        self.cards = ['A', '10', 'K', 'Q', 'J', '9']
        self.card_points = [11, 10, 4, 3, 2, 0]

    def get_card_points(self, card):
        card_index = self.cards.index(card[:len(card) - 1])
        points = self.card_points[card_index]
        return points

    def get_index_of_power(self, card):
        return self.cards.index(card[:len(card) - 1])
        
    def generate_deck(self):
        deck = []
        for suit in self.suits:
            for card in self.cards:
                deck.append(card + suit)
        return deck

    def get_suit_index_of_card(self, card):
        return self.suits.index(card[len(card) - 1])

    def compare_cards(self, card_one, card_two, trump_suit):
        if self.get_suit_index_of_card(card_one) != self.get_suit_index_of_card(card_two):
            if card_two[len(card_two) - 1] == trump_suit:
                return False
            return True
        else:
            if self.cards.index(card_one[:len(card_one) - 1]) < self.cards.index(card_two[:len(card_two) - 1]):
                return True