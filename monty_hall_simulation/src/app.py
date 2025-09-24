import streamlit as st
import pandas as pd
from monty_hall_simulation.src.monty_hall import play_monty_hall

st.title("Monty Hall Simulator", width=600)
st.title(	
":red[Paradox] :chart_with_upwards_trend:")

st.markdown("""
### Monty Hall Paradox 🚪
The Monty Hall Paradox is a famous probability puzzle based on a game show. A contestant picks one of three doors. Behind one door is a **car**, and behind the other two are **goats**.

---

### Why Switching Wins More 🏎️
After you pick a door, the host (who knows where the car is) opens a different door to reveal a goat. You are then given a choice: **stick** with your original door or **switch** to the other unopened door.

- **Sticking**: Your original choice had a **1/3** chance of being right. The host's action doesn't change this probability. If you stick with your first choice, you'll win about **33%** of the time.
- **Switching**: When you first chose, the other two doors collectively had a **2/3** chance of having the car. The host revealing a goat concentrates that entire **2/3** probability onto the single remaining unopened door. By switching, you're taking the higher probability, and will win about **67%** of the time.

The host's action gives you valuable new information, making switching the superior strategy.

###### Rememver As you select the door, host always reveal a Goat that is behind the other door 
""", unsafe_allow_html=True)

with st.sidebar:
  st.markdown(
    """
    ### Monty Hall Simulation
    In this app, the player doesn't choose a door. Instead, the app simulates the game many times to calculate the win/loss percentages for two different strategies:

    1.  **Staying** with the initial door.
    2.  **Switching** to the other unopened door.

    Your only role is to select a strategy and the number of times you want the game to be played. The results will then show you which strategy is more likely to win in the long run.
    """
)



  



  keep_the_selected_door = st.text_input("Do you want to keep the selected door? Only Yes or No", value="Yes").title()

  if keep_the_selected_door not in ["Yes", "No"]:
    st.error(f" Your Input {keep_the_selected_door} is not Valid, Only 'Yes' or 'No' is Acceptable!")
    keep_the_selected_door = st.text_input("Do you want to keep the selected door? Only Yes or No", value="Yes").title()


  Insert_numbers = st.number_input("Number of Try", min_value= 2, value=10)
  st.divider()
  
  st.image("image/mehdi_logo.png")

  
  
 

if keep_the_selected_door =="Yes" and Insert_numbers >=2:
  outcome = play_monty_hall(keep_your_door=True, number_of_play=Insert_numbers)
elif keep_the_selected_door == "No" and Insert_numbers >=2 :
  outcome = play_monty_hall(keep_your_door=False, number_of_play=Insert_numbers)

col1, col2 = st.columns(2)

col1.metric("Percentage of Winning The Game", outcome[0], border=True)
col2.metric("Percentage of Losing The Game", outcome[1], border=True)





col3, col4 = st.columns([outcome[0], outcome[1]])

with col1:
      st.markdown(
          f'<div style="background-color: #4CAF50; height:50px; border-radius:10px 0 0 10px;"></div>',
          unsafe_allow_html=True
      )
      st.markdown(f"**{outcome[0]*100}%**")
with col2:
  st.markdown(
      f'<div style="background-color: #F44336; height:50px; border-radius:0 10px 10px 0;"></div>',
      unsafe_allow_html=True
  )
  st.markdown(f"**{outcome[1]*100}%**")







