from turtle import Turtle

class Snake:
  INTIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
  MOVE_DISTANCE = 20

  def __init__(self) -> None:
    self.snake_body = []
    for _ in range(3):
      self.snake_segment = Turtle("square")
      self.snake_segment.color("white")
      self.snake_segment.penup()
      self.snake_body.append(self.snake_segment)
      self.snake_body[_].goto(self.INTIAL_POSITIONS[_])
    self.head = self.snake_body[0]

  def move(self):
    for snake_index in range(len(self.snake_body) - 1, 0, -1):
      x_pos = self.snake_body[snake_index - 1].xcor()
      y_pos = self.snake_body[snake_index - 1].ycor()
      self.snake_body[snake_index].goto(x_pos, y_pos)
    self.snake_body[0].forward(self.MOVE_DISTANCE)
      
  def up(self):
    if self.head.heading() == 270.0:
      return
    self.head.setheading(90)
  def down(self):
    if self.head.heading() == 90.0:
      return
    self.head.setheading(270)
  def left(self):
    if self.head.heading() == 0.0:
      return
    self.head.setheading(180)
  def right(self):
    if self.head.heading() == 180.0:
      return
    self.head.setheading(0)
