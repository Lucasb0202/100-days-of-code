import random
from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.penup()
    self.game_speed = 3
    self.setheading(random.randint(145, 215))

  def reflect(self):
    self.setheading(180 - self.heading())
    self.game_speed += 0.2

  def move(self):
    self.forward(self.game_speed)
    if self.ycor() <= -320 or self.ycor() >= 320:
      self.setheading(360 - self.heading())

  def reset(self, x_cor):
    if x_cor <= -430:
      self.setheading(random.randint(0, 55))
    elif x_cor >= 430:
      self.setheading(random.randint(145, 215))
    self.goto(0, 0)
    self.game_speed = 3