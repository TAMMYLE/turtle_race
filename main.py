from turtle import Turtle
from turtle import Screen
import random

sc = Screen()
sc.setup(width=500, height=400)

# Set state for the race
is_race_on = False

# List of colors
colors = ["medium violet red", "brown", "olive", "yellow", "medium blue", "cornflower blue"]

# Create a popup window ro ask user enter their bet turtle
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Set vertical coordinates for turtles
y_coor = [180, 120, 60, 0, -60, -140]
 
# Create 6 turtles

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    # Set coordinates for each turtle based on y_coor list
    new_turtle.goto(x=-230, y=y_coor[turtle_index])
    # Set colors for each turtles
    new_turtle.color(colors[turtle_index])
    # add turtle to all_turtles list
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        # check if x coordinate of the turtle reach the end (x = 230)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won. Winning turtle is {winning_turtle}")
            else:
                print(f"You've lost. Winning turtle is {winning_turtle}")
        else:        
            random_distance = random.randint(0, 10) # distance that ONE turtle is move forward
            turtle.forward(random_distance) # move that random turtle

sc.exitonclick()