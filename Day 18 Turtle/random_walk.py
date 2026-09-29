import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)
# Define standard directions (0=East, 90=North, 180=West, 270=South)
directions = [0,90,180,270]  
# Predefined color list
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"]
tim.circle(100)  #100 is radius
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
for _ in range(200):
    # tim.color(random.choice(colors))  # Pick a random color
    tim.color(random_color())  #random_color() function
    tim.pensize(width=10)
    tim.setheading(random.choice(directions)) # Pick a random grid direction
    tim.forward(30) #  # Move forward by 30 units
    tim.speed("fastest")


screen = Screen()
# Keep the window open until clicked
screen.exitonclick()




