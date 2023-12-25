import random
import time
import os

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4

def deal_cards():
    player_deck = []
    dealer_deck = []

    for _ in range(2):
        player_deck.append(cards.pop(random.randint(0, len(cards) - 1)))
        dealer_deck.append(cards.pop(random.randint(0, len(cards) - 1)))

    return player_deck, dealer_deck

def show_deck(deck):
    print(" ".join([str(card) for card in deck]))

def calculate_score(deck):
    score1 = 0
    score2 = 0

    for card in deck:
        if str(card).isdigit():
            score1 += int(card)
            score2 += int(card)
        elif card == "A":
            if score2 + 11 <= 21:
                score1 += 1
                score2 += 11
            else:
                score1 += 1
                score2 += 1
        else:  # Face cards
            score1 += 10
            score2 += 10

    final_score = score2 if score2 <= 21 else score1
    return final_score

def display_game_state(player_deck, dealer_deck, reveal_dealer=False):
    os.system("cls" if os.name == "nt" else "clear")  # Clear the console
    print("Blackjack\n")
    print("Player's Hand:")
    show_deck(player_deck)
    print("\nDealer's Hand:")
    if reveal_dealer:
        show_deck(dealer_deck)
    else:
        print("X", dealer_deck[1])  # Show only the second card of the dealer
    print("\n")

def hit(player_deck):
    player_deck.append(cards.pop(random.randint(0, len(cards) - 1)))

def stand(dealer_deck):
    while calculate_score(dealer_deck) < 17:
        dealer_deck.append(cards.pop(random.randint(0, len(cards) - 1)))

def blackjack():
    player_wins = 0
    dealer_wins = 0

    while True:
        player_deck, dealer_deck = deal_cards()
        player_score = 0
        dealer_score = 0

        # Display current game state
        display_game_state(player_deck, dealer_deck)
        time.sleep(1)

        # Check if player or dealer has blackjack
        if calculate_score(player_deck) == 21:
            print("Blackjack! You win!")
            player_wins += 1
        elif calculate_score(dealer_deck) == 21:
            print("Dealer has Blackjack. You lose.")
            dealer_wins += 1
        else:
            # Player's turn
            while True:
                choice = input("Do you want to hit or stand? ").lower()
                if choice == "hit" or choice == "h":
                    hit(player_deck)
                    display_game_state(player_deck, dealer_deck, reveal_dealer=False)
                    time.sleep(1)
                    player_score = calculate_score(player_deck)
                    if player_score > 21:
                        print("Busted! You lose.")
                        dealer_wins += 1
                        break
                elif choice == "stand" or choice == "s":
                    # Dealer's turn
                    stand(dealer_deck)
                    display_game_state(player_deck, dealer_deck, reveal_dealer=True)
                    time.sleep(1)

                    # Determine the winner
                    player_score = calculate_score(player_deck)
                    dealer_score = calculate_score(dealer_deck)
                    if dealer_score > 21:
                        print("Dealer busted! You win!")
                        player_wins += 1
                    elif player_score > dealer_score:
                        print("You win!")
                        player_wins += 1
                    elif player_score < dealer_score:
                        print("You lose.")
                        dealer_wins += 1
                    else:
                        print("It's a tie!")

                    break

        # Display scores
        print("\nScores - Player Wins: {}, Dealer Wins: {}\n".format(player_wins, dealer_wins))

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    blackjack()

