import turtle
from turtle import Turtle,Screen
import random

is_race_on=False
screen = Screen()
screen.title("Turtle Race")
screen.bgcolor("black")
screen.setup(width=800,height=500)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]


line_drawer = Turtle()
line_drawer.speed("fastest")
line_drawer.color("white")
line_drawer.penup()

"""Starting line"""
line_drawer.goto(-320, 150)
line_drawer.pendown()
line_drawer.goto(-320, -150)
line_drawer.penup()

"""Finish line"""
line_drawer.goto(250, 150)
line_drawer.pendown()
line_drawer.goto(250, -150)
line_drawer.hideturtle()

def display_result(message):
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.color("white")
    result_turtle.penup()
    result_turtle.goto(0, 0)
    result_turtle.write(message, align="center", font=("Arial", 24, "bold"))

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.shapesize(stretch_wid=1.5, stretch_len=1.5)
    new_turtle.goto(x=-300, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on :
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on=False

            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                display_result(f"You've won! The {winning_color} turtle is the winner!")
            else:
                display_result(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()