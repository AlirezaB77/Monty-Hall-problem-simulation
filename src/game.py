import random

def monty_hall(switch_doors):
    """
    Simulate a single game of the Monty Hall problem.

    Args:
    switch_doors (bool): True if the player switches doors, False otherwise.

    Returns:
    bool: True if the player wins (chooses the door with the car), False otherwise.
    """
    list_choice = ['car', 'goat', 'goat']
    random.shuffle(list_choice)
    initial_choice = random.choice(range(3))
    doors_revealed = [i for i in range(3) if i != initial_choice and list_choice[i] != 'car']
    door_revealed = random.choice(doors_revealed)
    
    if switch_doors:
        final_choice = [i for i in range(3) if i != door_revealed and i != initial_choice][0]
    else:
        final_choice = initial_choice
    
    return list_choice[final_choice] == "car"

def simulation_game(num_games):
    """
    Simulate multiple games of the Monty Hall problem and calculate win rates.

    Args:
    num_games (int): Number of games to simulate.

    Returns:
    tuple: A tuple containing two floats:
        - Win rate when not switching doors
        - Win rate when switching doors
    """
    wins_no_switch = sum([monty_hall(False) for _ in range(num_games)])
    wins_with_switch = sum([monty_hall(True) for _ in range(num_games)])
    
    return wins_no_switch , wins_with_switch

if __name__ == "__main__":
    num_games = 1000
    no_switch_rate, switch_rate = simulation_game(num_games)
    print(f"Win rate without switching: {no_switch_rate:.2%}")
    print(f"Win rate with switching: {switch_rate:.2%}")