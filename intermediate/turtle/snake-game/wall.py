from turtle import Turtle

class Wall(Turtle):
  def __init__(self):
    super().__init__()
    x = -260
    y = -260
    self.pencolor("white")
    self.penup()
    self.hideturtle()
    self.goto(x, y)
    self.width(10)
    for wall in range(4):
      if wall % 2 == 0:
        x *= -1
      else: y *= -1
      self.pendown()
      self.goto(x, y)

