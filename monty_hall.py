import random
from tabulate import tabulate

# Game statistics
stats = {"switch_wins": 0, "stick_wins": 0, "total_games": 0}

def get_valid_input(prompt, valid_options):
    """Prompt the user until they enter a valid input."""
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) in valid_options:
            return int(user_input)  # Return the valid choice as an integer
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(map(str, valid_options))}")

def print_doors(closed_doors, revealed_door=None, final_reveal=None):
    """Print big ASCII art for doors, revealing the car/goat or remaining closed."""
    door_art_closed = [
        "  _____   ",
        " |     |  ",
        " |     |  ",
        " |   {} |  ",
        " |     |  ",
        " |_____|  "
    ]

    door_art_goat = [
        "  _____   ",
        " |  G  |  ",
        " |  O  |  ",  # G for Goat
        " |  A  |  ",
        " |  T  |  ",
        " |_____|  "
    ]

    door_art_car = [
        "  _____   ",
        " |     |  ",
        " |  C  |  ",  # C for Car
        " |  A  |  ",
        " |  R  |  ",
        " |_____|  "
    ]

    doors_display = []
    for i in range(3):
        if final_reveal:
            # Final reveal (car or goat behind each door)
            doors_display.append(door_art_car if final_reveal[i] == "car" else door_art_goat)
        elif i == revealed_door:
            # Monty reveals the goat behind a door
            doors_display.append(door_art_goat)
        else:
            # Closed doors
            doors_display.append([line.format(i + 1) for line in door_art_closed])
    
    # Combine the ASCII lines for all doors to display them side by side
    for line in range(6):  # There are 6 lines in each door art
        print("   ".join(doors_display[door][line] for door in range(3)))

def monty_hall_game():
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    
    # Player picks a door
    print("Pick a door (1, 2, or 3):")
    print_doors([True, True, True])  # All doors closed
    player_choice = get_valid_input("Enter your choice: ", [1, 2, 3]) - 1
    
    # Monty opens a door that is not the player's choice and doesn't have the car
    remaining_doors = [i for i in range(3) if i != player_choice and doors[i] != "car"]
    monty_opens = random.choice(remaining_doors)
    
    print(f"Monty opens door {monty_opens + 1}, revealing a goat:")
    print_doors([i != monty_opens for i in range(3)], revealed_door=monty_opens)
    
    # Player's decision: switch or stay
    switch = get_valid_input("Would you like to switch your choice? (1 for Yes, 2 for No): ", [1, 2]) == 1
    if switch:
        player_choice = [i for i in range(3) if i != player_choice and i != monty_opens][0]
    
    # Final reveal
    print("Let's reveal what's behind the doors!")
    print_doors([False, False, False], final_reveal=doors)
    
    # Determine if the player won
    if doors[player_choice] == "car":
        print("Congratulations, you won the car! \n")
        print("============================================== \n")
        if switch:
            stats["switch_wins"] += 1
        else:
            stats["stick_wins"] += 1
    else:
        print("Sorry, you got a goat! \n")
        print("============================================== \n")
    
    stats["total_games"] += 1

def show_stats():
    """Show game statistics in a table."""
    switch_rate = stats["switch_wins"] / stats["total_games"] if stats["total_games"] else 0
    stick_rate = stats["stick_wins"] / stats["total_games"] if stats["total_games"] else 0
    table = [["Switch Wins", stats["switch_wins"]],
             ["Stick Wins", stats["stick_wins"]],
             ["Total Games", stats["total_games"]],
             ["Switch Win Rate", f"{switch_rate:.2%}"],
             ["Stick Win Rate", f"{stick_rate:.2%}"]]
    print(tabulate(table, headers=["Outcome", "Count"]))

def main():
    while True:
        monty_hall_game()
        print("Would you like to play again? (1 for Yes, 2 for No)")
        if get_valid_input("Enter your choice: ", [1, 2]) != 1:
            break
    
    show_stats()

if __name__ == "__main__":
    main()
