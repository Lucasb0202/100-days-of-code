from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10

class CarManager(Turtle):
  def __init__(self, x, y):
    super().__init__()
    self.car_speed = 5
    self.penup()
    self.shape("square")
    self.shapesize(stretch_len=2.5, stretch_wid=1)
    self.setheading(180)
    self.color(random.choice(COLORS))
    self.goto(x, y)

  def move(self, cars):
    self.forward(self.car_speed)
    for car in cars:
      if car.xcor() <= -330:
        cars.remove(car)
  
  def speed_increase(self):
    self.car_speed += MOVE_INCREMENT