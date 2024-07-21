# deck.py

import random
from card import Card
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in Card.suits:
            for ID in Card.id:
                self.all_cards.append(Card(suit,ID))

    def suffle(self):
        random.shuffle(self.all_cards)

    def remove(self):
        return self.all_cards.pop()