from turtle import Turtle

MOVE_DISTANCE = 50

class Player(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.speed(0)
    self.penup()
    self.shapesize(stretch_wid=1, stretch_len=4)
    self.color("white")
    self.goto(position)
    self.setheading(90)

  def up(self):
    self.forward(MOVE_DISTANCE)
    self.setheading(90)

  def down(self):
    self.forward(MOVE_DISTANCE)
    self.setheading(270)