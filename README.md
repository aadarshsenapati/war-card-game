# Card Game Project

## Overview
This project is a simple card game simulation implemented in Python. It includes classes to represent cards, a deck of cards, and players. The main functionality allows for shuffling a deck, drawing cards, and displaying a player's hand.

## Project Structure

- `Card` Class: Represents a single card with a suit and an identifier (rank).
- `Deck` Class: Represents a full deck of 52 cards and includes methods to shuffle the deck and draw a card.
- `Player` Class: Represents a player in the game, holding a hand of cards and providing methods to add, remove, and display cards.

## Classes and Methods

### Card Class
- **Attributes:**
  - `suits`: A list of suits with symbols.
  - `id`: A tuple of card ranks from 'Two' to 'Ace'.
  - `num`: A dictionary mapping card ranks to their numeric values.

- **Methods:**
  - `__init__(self, suits, id)`: Initializes a card with a given suit and rank.
  - `__str__(self)`: Returns a string representation of the card.

### Deck Class
- **Attributes:**
  - `all_cards`: A list to hold all the cards in the deck.

- **Methods:**
  - `__init__(self)`: Initializes the deck with 52 cards.
  - `shuffle(self)`: Shuffles the deck.
  - `remove(self)`: Removes and returns a card from the deck.

### Player Class
- **Attributes:**
  - `name`: The name of the player.
  - `all_cards`: A list to hold the player's cards.

- **Methods:**
  - `__init__(self, name)`: Initializes the player with a name.
  - `remove_one(self)`: Removes and returns the first card in the player's hand.
  - `remove_choice(self, n)`: Removes and returns the nth card in the player's hand.
  - `add_cards(self, new_cards)`: Adds new cards to the player's hand.
  - `show(self)`: Displays all cards in the player's hand.
  - `__str__(self)`: Returns a string representation of the player and the number of cards they have.

## Usage

Here is a basic example of how to use these classes:

```python
# Create a deck and shuffle it
deck = Deck()
deck.shuffle()

# Create two players
player1 = Player("Alice")
player2 = Player("Bob")

# Deal 5 cards to each player
for _ in range(5):
    player1.add_cards(deck.remove())
    player2.add_cards(deck.remove())

# Show each player's hand
player1.show()
player2.show()

# Print the player's hand size
print(player1)
print(player2)
```

## Requirements

- Python 3.x

## How to Run

1. Ensure you have Python installed.
2. Save the provided classes in a file named `classes.py`.
3. Create a separate script to use the classes, or run the example usage code in a Python interpreter.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
