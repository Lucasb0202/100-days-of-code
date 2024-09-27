import time
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from ball import Ball
from player import Player
from net import Net

screen = Screen()
screen.bgcolor("black")
screen.setup(900, 700)
screen.title("Pong")
screen.tracer(0)

net = Net()
ball = Ball()
player_1 = Player((-420, 0))
player_2 = Player((420, 0))
score = Scoreboard()

screen.listen()
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")
screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")

while True:
  screen.update()
  time.sleep(0.01)
  ball.move()

  if (player_1.distance(ball) <= 50 and ball.xcor() <= -400) or (player_2.distance(ball) <= 50 and ball.xcor() >= 400):
    ball.reflect()
  
  if ball.xcor() <= -430:
    score.increment_right()
    ball.reset(ball.xcor())

  if ball.xcor() >= 430:
    score.increment_left()
    ball.reset(ball.xcor())

screen.exitonclick()