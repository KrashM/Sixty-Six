from card_suit import Cards
from player import Player
from deck import Deck
from ai import AI
import random

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_one = Player(self.deck.deal_hand())
        #self.player_two = Player(self.deck.deal_hand())
        self.ai = AI(self.deck.deal_hand())
        self.trump_suit = self.deck.get_trump_suit()
        #print(self.trump_suit)
        self.player_one_on_hand = True
        self.runtime()

    def turn(self):
        #print(f"{self.player_one.get_hand()}     {self.ai.get_hand()}")
        player_one_choice = 0
        player_two_choice = self.ai.select(self.player_one.get_card_from_hand(player_one_choice), self.trump_suit)
        #player_two_choice = random.randint(0, self.player_two.get_hand_size() - 1)

        card1 = self.player_one.get_card_from_hand(player_one_choice)
        card2 = self.ai.get_card_from_hand(player_two_choice)

        if self.player_one_on_hand:
            self.grab(card1, card2)
        else:
            self.grab(card2, card1)
        
        self.draw(card1, card2)

    def draw(self, card1, card2):
        self.player_one.remove_card_from_hand(card1)
        self.ai.remove_card_from_hand(card2)

        if self.deck.get_deck_size():
            if self.player_one_on_hand:
                self.player_one.add_to_hand(self.deck.draw())
                self.ai.add_to_hand(self.deck.draw())
            else:
                self.ai.add_to_hand(self.deck.draw())
                self.player_one.add_to_hand(self.deck.draw())

    def grab(self, p1_card, p2_card):
        cards = Cards()
        if cards.compare_cards(p1_card, p2_card, self.trump_suit):
            if not self.player_one_on_hand:
                self.player_one_on_hand = False
                self.ai.add_to_pile(p1_card, p2_card)
            else:
                self.player_one_on_hand = True
                self.player_one.add_to_pile(p1_card, p2_card)
        else:
            if self.player_one_on_hand:
                self.player_one_on_hand = False
                self.ai.add_to_pile(p1_card, p2_card)
            else:
                self.player_one_on_hand = True
                self.player_one.add_to_pile(p1_card, p2_card)
        
    def runtime(self):
        while self.player_one.get_hand():
            self.turn()
        # print(self.player_one.get_pile())
        # print(self.ai.get_pile())
        # print(self.player_one.get_points())
        # print(self.ai.get_points())

    def win(self):
        if self.player_one.get_points() > self.ai.get_points():
            return True
        return False