import random
from turtle import Turtle

class Food(Turtle):
  def __init__(self) -> None:
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(0.75, 0.75)
    self.color("red")
    self.speed(0)
    self.refresh()
  
  def refresh(self):
    self.goto(random.randint(-240, 240), random.randint(-240, 240))
