import random
from turtle import Turtle, Screen, colormode

turtle = Turtle()

colormode(255)

def change_colour():
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)

  return R, G, B

def draw_shapes(num_sides):
  R, G, B = change_colour()
  angle = 360 / num_sides
  turtle.pencolor(R, G, B)
  for _ in range(num_sides):
    turtle.right(angle)
    turtle.forward(100)
  num_sides += 1
  if num_sides <= 10:
    draw_shapes(num_sides)

draw_shapes(3)

screen = Screen()
screen.exitonclick()