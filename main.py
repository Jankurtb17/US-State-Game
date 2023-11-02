import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
score = 0
# Read CSV File
data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
  user_guess = screen.textinput(title=f"{score} / 50 States Correct", prompt="What's another state's name").title()
  if user_guess == "Exit":
    missing_states = []
    for item in all_states:
      if item not in guessed_states:
        missing_states.append(item)
    # create data frame
    data = pd.DataFrame(missing_states)
    # dataframe to csv
    data.to_csv('states_to_learn.csv')
    break
  if user_guess in all_states:
    if user_guess not in guessed_states:
      guessed_states.append(user_guess)
      score += 1

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == user_guess]
    t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
    t.write(state_data.state.item())





turtle.mainloop()