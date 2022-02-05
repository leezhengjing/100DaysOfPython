import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.setup(width=729, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data['state'].to_list()
print(state_list)

state = State()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state_list:
        guessed_states.append(answer_state)
        state_data = data[data['state'] == answer_state]
        x_coordinate = (int(state_data['x']))
        y_coordinate = (int(state_data['y']))
        state.update_state(x_coordinate, y_coordinate, answer_state)

