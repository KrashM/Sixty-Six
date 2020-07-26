from card_suit import Cards
import random

class Deck:
    def __init__(self):
        cards = Cards()
        self.deck = cards.generate_deck()
        self.shuffle_deck()

    def shuffle_deck(self):
        for i in range(3):
            random.shuffle(self.deck)

    def get_trump_suit(self):
        card = self.deck[len(self.deck) - 1]
        self.deck.insert(0, card)
        self.deck.pop()
        return card[len(card) - 1]

    def get_deck(self):
        return self.deck

    def get_deck_size(self):
        return len(self.deck)

    def deal_hand(self):
        cards = []
        for i in range(6):
            cards.append(self.deck[len(self.deck) - 1])
            self.deck.pop()
        return cards

    def draw(self):
        card = self.deck[len(self.deck) - 1]
        self.deck.pop()
        return card