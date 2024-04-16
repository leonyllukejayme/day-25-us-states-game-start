import turtle
import pandas as pd

screen =  turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725,height=491)
screen.cv._rootwindow.resizable(False,False)

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
d = pd.read_csv('50_states.csv')
all_states = d.state.to_list()

# playing = True
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 State",prompt="What's another states name?").title()

    if answer_state == "Exit":
        states_to_learn = all_states
        for gs in guess_state:
            states_to_learn.remove(gs)
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        x = int(d[d.state == answer_state].x.iloc[0])
        y = int(d[d.state == answer_state].y.iloc[0])

        ste_loc = turtle.Turtle()
        ste_loc.penup()
        ste_loc.hideturtle()
        ste_loc.goto(x,y)
        ste_loc.write(answer_state,align='center')
        guess_state.append(answer_state)


# print(states_to_learn)
print(len(states_to_learn))

# data_dict = {
#     "missed_states": states_to_learn
# }

# states_to_learn.csv







# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


# screen.mainloop()