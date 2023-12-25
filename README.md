# Blackjack Game

Welcome to a text-based Blackjack game implemented in Python. This game allows you to play rounds of Blackjack against a dealer while keeping track of your and the dealer's scores.

## Instructions

1. Run the script in a Python environment to start the game.
2. Follow the prompts to decide whether to hit or stand during your turn.
3. The game will automatically play the dealer's turn according to standard Blackjack rules.
4. The winner of each round is determined, and scores are displayed.
5. You can choose to play again or exit the game.

## Rules

- The game adheres to standard Blackjack rules, where the goal is to have a hand value as close to 21 as possible without exceeding it.
- Face cards have a value of 10, and Aces can be counted as 1 or 11, depending on the situation.
- Players can choose to hit (draw a card) or stand (keep the current hand).
- The dealer must hit until their hand value is at least 17.

## Functions

### `deal_cards()`

- **Input:** None
- **Output:** Tuple (player_deck, dealer_deck)

This function deals two cards to both the player and the dealer, returning their initial decks.

### `show_deck(deck)`

- **Input:** List of cards (`deck`)
- **Output:** None

Prints the cards in the given deck, used for displaying the player's and dealer's hands.

### `calculate_score(deck)`

- **Input:** List of cards (`deck`)
- **Output:** Integer (final_score)

Calculates the final score of a given deck, considering Aces as 1 or 11 based on the best scenario to avoid busting.

### `display_game_state(player_deck, dealer_deck, reveal_dealer=False)`

- **Input:** Lists of cards (`player_deck`, `dealer_deck`), Boolean (`reveal_dealer`)
- **Output:** None

Displays the current game state, showing the player's and dealer's hands. If `reveal_dealer` is False, only the first card of the dealer is shown.

### `hit(player_deck)`

- **Input:** List of cards (`player_deck`)
- **Output:** None

Simulates the player choosing to hit, adding a card to their deck.

### `stand(dealer_deck)`

- **Input:** List of cards (`dealer_deck`)
- **Output:** None

Simulates the player choosing to stand, allowing the dealer to draw cards until their hand value is at least 17.

### `blackjack()`

- **Input:** None
- **Output:** None

Main game loop that manages the flow of the game, dealing cards, displaying the game state, and determining the winner.

### `main()`

- **Input:** None
- **Output:** None

Executes the `blackjack()` function when the script is run.

## Running the Game

Ensure that you have a Python environment installed, then execute the script:

```bash
python blackjack_game.py
