import random

# Function to simulate rolling a dice
def roll_dice():
    return random.randint(1, 6)

def ludo_game():
    print("Welcome to the Text-Based Ludo Game!")
    print("Two players will take turns to roll the dice.")
    print("The first player to reach or exceed position 30 wins!\n")

    # Initialize player positions
    player_positions = {"Player 1": 0, "Player 2": 0}

    # Explain the rules to the user
    print("Game Rules:")
    print("1. Each player takes turns to roll the dice.")
    print("2. The dice roll determines how many steps the player moves forward.")
    print("3. The first player to reach or exceed position 30 wins the game.\n")

    while True:
        for player in player_positions:
            input(f"{player}, press Enter to roll the dice...")
            dice_roll = roll_dice()
            print(f"{player} rolled a {dice_roll}!")

            # Update player position
            player_positions[player] += dice_roll
            print(f"{player}'s new position: {player_positions[player]}\n")

            # Check for a winner
            if player_positions[player] >= 30:
                print(f"Congratulations, {player}! You win! 🎉")
                print("Thanks for playing the Ludo Game!\n")

                # Ask if the players want to play again
                play_again = input("Do you want to play again? (yes/no): ").strip().lower()
                if play_again == "yes":
                    print("Restarting the game...\n")
                    ludo_game()
                else:
                    print("Goodbye! Hope to see you again soon. 👋")
                return

if __name__ == "__main__":
    ludo_game()