# player.py

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
    
