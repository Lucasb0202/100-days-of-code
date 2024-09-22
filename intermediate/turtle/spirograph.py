import random
from turtle import Turtle, Screen, colormode

turtle = Turtle()

colormode(255)
turtle.speed(0)

def change_colour():
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)

  return (R, G, B)


def draw_spirograph(tilt_size):
  heading = turtle.heading()
  for _ in range(int(360 / tilt_size)):
    turtle.color(change_colour())
    turtle.circle(100)
    heading += tilt_size
    turtle.setheading(heading)
  
draw_spirograph(5)

screen = Screen()
screen.exitonclick()