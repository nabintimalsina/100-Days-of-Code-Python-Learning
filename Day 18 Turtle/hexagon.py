import turtle as t
from turtle import Screen
import random

tim = t.Turtle()

colours = ["red", "blue", "brown", "green", "Yellow", "white"]
#360/5 = 72 in each 5 sides
def draw_shape(number_of_sides):
    angle = 360/number_of_sides
    for _ in range(number_of_sides):  #1 to 5
        tim.forward(100)  
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen() #screen holds the window object.
screen.exitonclick() #Keeps the pop-up window open until you physically click on it with your mouse, preventing the window from closing instantly when the code finishes




