from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
wall = Wall()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
  time.sleep(0.05)
  snake.move()
  screen.update()

  if snake.head.distance(food) < 25:
    food.refresh()
    score.increment()
    snake.grow()

  if snake.head.xcor() > 240  or snake.head.ycor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() < -240:
    snake.reset()
    score.reset()
    # score.game_over()
    # break

  for segment in snake.snake_body[1:]:
    if snake.head.distance(segment) < 1:
      snake.reset()
      score.reset()
      # score.game_over()
      # game_on = False
      # break

screen.exitonclick()


