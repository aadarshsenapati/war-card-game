# classes.py


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
    

import random
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
    


class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]


    def remove_one(self):
        return self.all_cards.pop(0)
    
    def remove_choice(self,n):
        return self.all_cards.pop(n)

    def add_cards(self,new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


    def show(self):
        print("Your deck is: ")
        num = 1
        for i in self.all_cards:
            
            print(f"{num}) {i}")
            num += 1

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'