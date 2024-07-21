# card.py

class Card:
    suits=['Heart: ❤️','Spades: ♠️','Diamonds: ♦️','Clubs: ♣️']
    id=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    num={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
    def __init__(self,suits,id):
        self.id=id
        self.suits=suits
        self.num = Card.num [id]
    def __str__(self):
        return self.id + ' of '+self.suits
    