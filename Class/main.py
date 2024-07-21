# main.py

from classes import Player,Deck
player_one=Player(input("Enter your name: "))
player_two=Player("Computer")


def end(score):
    print(f"Your score is: {score}\nYou have {len(player_one.all_cards)} cards")

def main():
    score=0
    new_deck=Deck()
    new_deck.suffle()

    for _ in range(26):
        player_one.add_cards(new_deck.remove())
        player_two.add_cards(new_deck.remove())

    print(player_one.show())

    game = True
    round=0

    while game:
        round=round+1
        print("Round: ",round)

        if len(player_one.all_cards) == 0:
            print("Player One out of cards! Game Over")
            print("Player Two Wins!")
            end(score)
            game = False
            break

        if len(player_two.all_cards) == 0:
            print("Player Two out of cards! Game Over")
            print("Player One Wins!")
            end(score)
            game = False
            break

        player_one.show()

        player_one_cards = []
    
        while True:
            try:
                print("Type 192640 to exit")
                n = int(input("Choose the card (1 to {}): ".format(len(player_one.all_cards))))
                if n== 192640:
                    print("Game over!")
                    end(score)
                    return
                if 1 <= n <= len(player_one.all_cards):
                    player_one_cards = [player_one.remove_choice(n - 1)]
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Enter a number.")

    
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())
    

        war = True
        while war:
            if player_one_cards[-1].num > player_two_cards[-1].num:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                print("Player 1 lost! Computer Won!")
                war = False
        
            elif player_one_cards[-1].num < player_two_cards[-1].num:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                score+=1
                print("Player 1 won! Computer lost!")
                war = False
        
            else:
                print("War!")
                if len(player_one.all_cards) < 5:
                    print("Player One unable to play war! Game Over at War")
                    print("Player Two Wins! Player One Loses!")
                    end(score)
                    game= False
                    break
                elif len(player_two.all_cards) < 5:
                    print("Player Two unable to play war! Game Over at War")
                    print("Player One Wins! Player One Loses!")
                    end(score)
                    game = False
                    break
                else:
                    for _ in range(5):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())

if __name__ == "__main__":
    main()