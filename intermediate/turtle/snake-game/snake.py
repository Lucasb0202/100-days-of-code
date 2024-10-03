from turtle import Turtle

class Snake:
  MOVE_DISTANCE = 12.5

  def __init__(self) -> None:
    self.snake_body = []
    for _ in range(3):
      self.snake_segment = Turtle("square")
      self.snake_segment.color("white")
      self.snake_segment.penup()
      self.snake_body.append(self.snake_segment)
      self.snake_body[_].goto(_ * -20, 0)
    self.head = self.snake_body[0]

  def move(self):
    for snake_index in range(len(self.snake_body) - 1, 0, -1):
      x_pos = self.snake_body[snake_index - 1].xcor()
      y_pos = self.snake_body[snake_index - 1].ycor()
      self.snake_body[snake_index].goto(x_pos, y_pos)
    self.snake_body[0].forward(self.MOVE_DISTANCE)

  def grow(self):
    self.snake_segment = Turtle("square")
    self.snake_segment.color("white")
    self.snake_segment.penup()
    self.snake_body.append(self.snake_segment)
      
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

  def reset(self):
    for i in range(len(self.snake_body)):
        self.snake_body[i].goto(1000, 1000)
    self.snake_body.clear()
    for i in range(3):
      self.snake_segment = Turtle("square")
      self.snake_segment.color("white")
      self.snake_segment.penup()
      self.snake_body.append(self.snake_segment)
      self.snake_body[i].goto(i * -20, 0)
    self.head = self.snake_body[0]

