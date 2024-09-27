from turtle import Turtle

class Net(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.width(5)
    self.penup()
    self.color("white")
    self.setheading(270)
    self.goto(0, 325)
    self.speed(0)
    while self.ycor() >= -325:
      self.pendown()
      self.forward(10)
      self.penup()
      self.forward(15)