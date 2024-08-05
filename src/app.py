import streamlit as st
import time
from game import simulation_game

"""
Run a Monty Hall problem simulation using Streamlit.

This function creates a Streamlit app that allows users to input the number of games
to simulate. It then runs the simulation, updating two line charts in real-time to show
the win rates for both switching and not switching strategies.

The simulation uses the simulation_game function from the game module.

Streamlit Elements:
- Title
- Number input for game count
- Two columns with subheaders and line charts for each strategy
"""
st.title(":sparkles: Monty Hall Problem :sparkles:")

number = st.number_input("Enter the game number", min_value=1, max_value=10000, value=100)

col1, col2 = st.columns(2)
col1.subheader("Win rate without switching")
col2.subheader("Win rate with switching")

chart1 = col1.line_chart(x=None, y=None)
chart2 = col2.line_chart(x=None, y=None)

wins_no_switch = 0
wins_switch = 0

for i in range(number):
    num_wins_no_switch, num_wins_with_switch = simulation_game(1)
    wins_no_switch += num_wins_no_switch
    wins_switch += num_wins_with_switch

    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
    time.sleep(0.05)