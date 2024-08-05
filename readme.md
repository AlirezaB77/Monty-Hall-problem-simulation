# Monty Hall Problem Simulator

## Overview

This Python script simulates the famous Monty Hall problem, a probability puzzle named after the host of the television game show Let's Make a Deal. The simulation demonstrates the counter-intuitive result that switching doors in the game show scenario significantly increases the chances of winning.

## The Monty Hall Problem

In the Monty Hall problem:

1. A contestant is presented with three doors.
2. Behind one door is a car (the prize), and behind the other two are goats.
3. The contestant picks a door.
4. The host, who knows what's behind each door, opens another door which has a goat.
5. The contestant is then given the option to stick with their original choice or switch to the remaining unopened door.

The question is: Should the contestant switch doors to maximize their chances of winning the car?

## Features

- Simulates individual games of the Monty Hall problem
- Runs multiple simulations to calculate win rates for both switching and not switching strategies
- Provides clear output of win percentages for each strategy

## Usage

To run the simulation:

1. Ensure you have Python installed on your system.
2. Save the script as `monty_hall_simulator.py`.
3. Run the script from the command line:
4. The script will simulate 1000 games by default and output the win rates for both strategies.

## Customization

You can modify the `num_games` variable in the `if __name__ == "__main__":` block to change the number of simulations.

## Results

The simulation typically shows that:
- Staying with the original door wins about 1/3 of the time.
- Switching doors wins about 2/3 of the time.

These results confirm the mathematical probability and demonstrate why switching is the optimal strategy in the Monty Hall problem.

