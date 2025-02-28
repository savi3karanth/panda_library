import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess State of US")
image = "us_blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_state = []

data = pandas.read_csv('us_50_states.csv')
all_states = data.state.to_list()
print(all_states)

while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 states correct", prompt="Guess another state").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in all_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

screen.exitonclick()