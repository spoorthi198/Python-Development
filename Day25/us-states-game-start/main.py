import turtle
import pandas
screen = turtle.Screen()

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# is_game_on = True
# while is_game_on:



data = pandas.read_csv("50_states.csv")
all_states=data["state"].to_list()
print(all_states)
# print(data[data["state"] == guess])


# print(map_locaton.x)
# print(map_locaton.y)
# print(map_locaton.state)



guessed_state = []
while len(guessed_state) <50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct ", prompt="whats another states name?")
    guess = answer_state.title()
    map_location = data[data["state"] == guess]
    guessed_state.append(guess)


    if guess == 'Exit':
        missing_state = []

        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        print(missing_state)
        new_states = pandas.DataFrame(missing_state)
        new_states.to_csv("new_states_to_learn.csv")
        break
    if guess in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        t.goto(int(map_location.x),int(map_location.y))
        t.write(map_location.state.item())

# screen will remain even after completing the execution
# turtle.mainloop()

screen.exitonclick()