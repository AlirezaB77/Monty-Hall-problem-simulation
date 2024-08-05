# Monty Hall Problem Simulator with Streamlit

## Overview

This project provides an interactive web application to simulate and visualize the famous Monty Hall problem using Streamlit. It allows users to run multiple simulations and observe the win rates for both switching and not switching strategies in real-time.

## The Monty Hall Problem

The Monty Hall problem is a probability puzzle based on a game show scenario:

1. A contestant faces three doors.
2. Behind one door is a car (the prize), and goats are behind the other two.
3. The contestant picks a door.
4. The host, knowing what's behind each door, opens a non-chosen door revealing a goat.
5. The contestant can then stick with their original choice or switch to the remaining unopened door.

The puzzle explores whether switching doors increases the chances of winning the car.

## Features

- Interactive web interface using Streamlit
- User-defined number of simulations (1 to 10,000)
- Real-time visualization of win rates for both strategies
- Dynamic line charts showing the evolution of win rates as simulations progress

## Requirements

- Python 3.6+
- Streamlit
- Custom `game` module (containing the `simulation_game` function)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/AlirezaB77/monty-hall-streamlit.git
   cd monty-hall-streamlit
   ```

2. Install the required packages:
   ```
   pip install streamlit
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open the provided local URL in your web browser.

3. Enter the desired number of games to simulate (between 1 and 10,000).

4. Watch the real-time charts update as the simulations run.

## File Structure

- `app.py`: The main Streamlit application
- `game.py`: Module containing the `simulation_game` function
- `README.md`: This file

## Customization

You can modify the `app.py` file to change the simulation parameters, chart styles, or add additional features to the Streamlit interface.

