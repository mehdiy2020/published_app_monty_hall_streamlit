# published_app_monty_hall_streamlit
# Monty Hall Simulator
This is a Streamlit application that simulates the classic Monty Hall problem to demonstrate the counter-intuitive probabilities behind it. The app allows users to choose a strategy—either "stay" with their initial door or "switch" to the other remaining door—and then runs a simulation over a specified number of trials to show the long-term winning percentages.

## 🎲 The Monty Hall Paradox
The paradox is a probability puzzle based on a game show. A contestant selects one of three doors. Behind one door is a car, and behind the other two are goats. After the contestant makes their initial choice, the host (who knows where the car is) opens one of the two unpicked doors to reveal a goat. The contestant is then given the option to stick with their original choice or switch to the other unopened door.

The surprising solution is that the odds of winning are significantly higher if the contestant switches their choice.

## 💻 How the App Works
This application eliminates the need for a user to play a single game. Instead, it automates the process to prove the statistical outcome:

Strategy Selection: The user selects a strategy: Stay or Switch.

Trial Simulation: The app runs the game hundreds or thousands of times in the background.

Statistical Results: The results are presented as win/loss percentages, visually demonstrating why the "switch" strategy is superior.

🚀 Getting Started
Clone the repository (if it's in a git repository)
git clone `<repository_url>`

Navigate to the project directory
cd monty-hall-simulator

Install the required libraries
pip install -r requirements.txt

Run the app
streamlit run src/app.py

📁 File Structure
The project is structured as follows:

.
├── src/
│   ├── app.py              # The Streamlit application interface.
│   └── monty_hall.py       # Contains the core simulation logic.
└── requirements.txt        # Lists the project dependencies.
└── README.md