import random
from tabulate import tabulate

# Game statistics
stats = {"switch_wins": 0, "stick_wins": 0, "total_games": 0}

def print_doors(closed_doors, revealed_door=None, final_reveal=None):
    """Print ASCII art for doors, revealing the car/goat or remaining closed."""
    door_art = []
    for i, closed in enumerate(closed_doors):
        if final_reveal:
            door_art.append("| C |" if final_reveal[i] == "car" else "| G |")
        elif i == revealed_door:
            door_art.append("| G |")
        else:
            door_art.append("|---|" if closed else "|   |")
    print("   ".join(door_art))
    print("  1     2     3")

def monty_hall_game():
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    
    # Player picks a door
    print("Pick a door (1, 2, or 3):")
    print_doors([True, True, True])  # All doors closed
    player_choice = int(input()) - 1
    
    # Monty opens a door that is not the player's choice and doesn't have the car
    remaining_doors = [i for i in range(3) if i != player_choice and doors[i] != "car"]
    monty_opens = random.choice(remaining_doors)
    
    print(f"Monty opens door {monty_opens + 1}, revealing a goat:")
    print_doors([i != monty_opens for i in range(3)], revealed_door=monty_opens)
    
    # Player's decision: switch or stay
    print("Would you like to switch your choice? (y/n):")
    switch = input().lower() == "y"
    if switch:
        player_choice = [i for i in range(3) if i != player_choice and i != monty_opens][0]
    
    # Final reveal
    print("Let's reveal what's behind the doors!")
    print_doors([False, False, False], final_reveal=doors)
    
    # Determine if the player won
    if doors[player_choice] == "car":
        print("Congratulations, you won the car!")
        if switch:
            stats["switch_wins"] += 1
        else:
            stats["stick_wins"] += 1
    else:
        print("Sorry, you got a goat!")
    
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
        print("Would you like to play again? (y/n)")
        if input().lower() != "y":
            break
    
    show_stats()

if __name__ == "__main__":
    main()
