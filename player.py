from card_suit import Cards

class Player:
    def __init__(self, starting_hand):
        self.hand = starting_hand
        self.pile =  []
        self.points = 0

    def evaluate(self):
        cards = Cards()
        for card in self.pile:
            round_points = cards.get_card_points(card[0]) + cards.get_card_points(card[1])
            self.points += round_points

    def add_to_hand(self, card):
        self.hand.append(card)

    def add_to_pile(self, card1, card2):
        self.pile.append([card1, card2])

    def get_pile(self):
        return self.pile

    def get_hand(self):
        return self.hand

    def get_hand_size(self):
        return len(self.hand)

    def get_card_from_hand(self, index):
        return self.hand[index]

    def remove_card_from_hand(self, card):
        if card not in self.hand:
            return
        else:
            self.hand.remove(card)

    def get_points(self):
        self.evaluate()
        return self.points
