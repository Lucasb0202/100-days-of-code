import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

cars = []
i = 0
while i < 15:
  cars.append(CarManager(random.randint(310, 500), random.randint(-280, 270)))
  i += 1

car_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_counter % 5 == 0:
      cars.append(CarManager(random.randint(310, 800), random.randint(-280, 270)))
    for car in cars:
      car.move(cars)
    car_counter += 1

    if player.ycor() >= 270:
      score.increase_level()
      player.reset()
      for car in cars:
        car.speed_increase()
    