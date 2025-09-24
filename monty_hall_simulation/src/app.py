import streamlit as st
from random import choice, shuffle
from typing import Tuple



def select_the_door(select_door_automatically: bool=True) -> Tuple[list, str]:
  """To select one of the three doors to start the Monty Hall Game.
  Player may decide the door be selected randomly 
  by seting the argument to True which is the default.

  :param select_door_automatically: If player choose to 
  select the door manualy the argument can be set to Fasle, defaults to True
  :type select_door_automatically: bool, optional
  :return: Returns a tuple with a list up to two elements in it, a string of selected door!
  :rtype: It returns a Tuple
  """

  main_list = ['Goat', 'Goat', 'Porsche']
  shuffle(main_list)
  main_dict = {"door_1": main_list[0], "door_2": main_list[1], 'door_3':main_list[2]}
  selection_list = ["a", "b", "c"]
  if not select_door_automatically:
    select_a_door = (input("Enter one of A, B, or C door: ")).lower()
    while select_a_door not in selection_list:
      select_a_door = (input("Enter one of A, B, or C door: ")).lower()
  else:
    select_a_door = choice(selection_list)
 
  main_dict_1 = main_dict
  if select_a_door == "a":
    contestant_door = main_dict_1["door_1"]
    print("You have selected door # 1")
    del main_dict_1["door_1"]
  elif select_a_door =="b":
    contestant_door = main_dict_1["door_2"]
    print("You have selected door # 2")
    del main_dict_1["door_2"]
  elif select_a_door =="c":
    contestant_door = main_dict_1["door_3"]
    print("You have selected door # 3")
    del main_dict_1["door_3"]
  return main_dict_1, contestant_door



def play_monty_hall(keep_your_door: bool=True, number_of_play: int=10) -> Tuple[float, float]:
  """Simulates the Monty Hall game for a specified number of plays.

  This function runs a simulation of the Monty Hall problem. The player's
  strategy (to keep or switch doors) is determined by the `keep_your_door`
  parameter. The simulation automatically runs for `number_of_play` rounds,
  tracking the win and loss rates. 

  :param keep_your_door: A boolean indicating the player's strategy. If True,
  the player keeps their initial door selection. If False,
  the player switches to the other remaining door. Defaults to True.
  :type keep_your_door: bool, optional
  :param number_of_play: The number of times the game is simulated., defaults to 10
  :type number_of_play: int, optional
  :return: A tuple containing the winning and losing percentages, rounded to three
  decimal places.
  :rtype: Tuple
  """
  number_of_winning = 0
  number_of_losing = 0
  play_turn = 1
  while play_turn < number_of_play + 1:
    
    outcome = select_the_door()
    goat_door = [key for key, value in outcome[0].items() if value == "Goat"]
    door_to_reveal = choice(goat_door)
    print(f"{door_to_reveal} will be opened and {outcome[0][door_to_reveal]} is revealed!")
    del outcome[0][door_to_reveal]
    
    if keep_your_door and outcome[1] == "Porsche":
        number_of_winning +=1
        play_turn +=1
    elif keep_your_door and outcome[1] == "Goat":
        number_of_losing +=1
        play_turn +=1
    elif not keep_your_door and tuple(outcome[0].values())[0] == "Porsche":
      number_of_winning +=1
      play_turn +=1
    elif not keep_your_door and  tuple(outcome[0].values())[0] == "Goat":
      number_of_losing +=1
      play_turn +=1
  winning_percent = round(number_of_winning/number_of_play, ndigits=3)
  losing_percent = round(number_of_losing/number_of_play, ndigits=3)
  print(f"Game has the chanse of winning {winning_percent}% and losing {losing_percent}%")
  return winning_percent, losing_percent 



st.title("Monty Hall Simulator", width=600)
st.title(	
":red[Paradox] :chart_with_upwards_trend:")

st.markdown("""
### Monty Hall Paradox 🚪
The Monty Hall Paradox is a famous probability puzzle based on a game show. A contestant picks one of three doors. Behind one door is a **car**, and behind the other two are **goats**.

---
### Why Switching Wins More 🏎️
When you first choose, your door has a 1/3 chance of winning. The other two doors, combined, have a 2/3 chance. The host's action of revealing a goat behind one of them doesn't change those initial probabilities. Instead, it concentrates the entire 2/3 chance onto the single remaining unopened door.

Therefore, sticking keeps your original 1/3 chance, while switching gives you a 2/3 chance of winning.

###### Rememver As you select the door, host always reveal a Goat that is behind the other door 
""", unsafe_allow_html=True)

with st.sidebar:
  st.markdown(
    """
    ### Monty Hall Simulation
    This app simulates the Monty Hall game many times to prove which strategy is better: staying with your initial choice or switching to the other door.

    You simply select a strategy and the number of games to play. The results will show you the win/loss percentages for each strategy, revealing which one is more likely to win over time.
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







