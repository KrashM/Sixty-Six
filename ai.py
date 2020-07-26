from card_suit import Cards
from player import Player
import random

class AI(Player):
    def select(self, human_card, trump_suit):
        cards = Cards()
        trump_card = -1
        for i in range(len(self.hand)):
            if human_card[len(human_card) - 1] in self.hand[i] and cards.get_index_of_power(human_card) > cards.get_index_of_power(self.hand[i]):
                return i
            elif self.hand[i][len(self.hand[i]) - 1] == trump_suit and cards.get_index_of_power(self.hand[i]) > trump_card:
                trump_card = i
        if trump_card > -1:
            return trump_card
        return random.randint(0, len(self.hand) - 1)
