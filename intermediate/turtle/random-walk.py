import random
from turtle import Turtle, Screen, colormode

turtle = Turtle()

colormode(255)
turtle.width(10)
turtle.speed(0)

directions = [0, 90, 180, 270]

def change_colour():
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)

  return (R, G, B)

while True:
  turtle.color(change_colour())
  turtle.setheading(random.choice(directions))
  turtle.forward(30)

screen = Screen()
screen.exitonclick()