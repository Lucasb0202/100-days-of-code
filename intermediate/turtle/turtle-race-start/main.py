import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

def draw_finish_line():
  finish_line = Turtle()
  finish_line.speed(0)
  finish_line.hideturtle()
  finish_line.penup()
  finish_line.setpos(220, 210)
  finish_line.pendown()
  finish_line.sety(-210)

def start_game():
  draw_finish_line()
  user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour: ")
  racing = True
  turtles = []
  colours = ["red", "orange", "yellow", "green", "blue", "purple"]

  for i in range(6):
    turtles.append(Turtle("turtle"))

  y = -100
  for i in range(6):
    turtles[i].color(colours[i])  
    turtles[i].penup()
    turtles[i].goto(-230, y)
    y += 30  

  while racing:
    for i in range(6):
      turtles[i].forward(random.randint(0, 10))
      if turtles[i].pos()[0] >= 230:
        racing = False
        print(f"{turtles[i].pencolor().title()} won!")
        if user_bet.lower() == turtles[i].pencolor():
          print(f"Your bet: {user_bet.title()}. You won!")
        else: print(f"Your bet: {user_bet.title()}. You lost!")
        break
    
start_game()
screen.exitonclick()