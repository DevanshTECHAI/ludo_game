import random

def roll_dice():
    return random.randint(1, 6)

def ludo_game():
    print("Welcome to the Text-Based Ludo Game!")
    print("Two players will take turns to roll the dice.")
    print("The first player to reach or exceed position 30 wins!\n")

    # Initialize player positions
    player_positions = {"Player 1": 0, "Player 2": 0}
    
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
                return

if __name__ == "__main__":
    ludo_game()