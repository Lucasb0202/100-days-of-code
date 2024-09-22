from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.speed(0)

def move_forwards():
  t.forward(10)

def move_backwards():
  t.back(10)

def turn_left():
  t.left(5)

def turn_right():
  t.right(5)

def clear_screen():
  t.clear()
  t.penup()
  t.setpos(0, 0)
  t.pendown()
  
screen.listen()

screen.onkeypress(move_forwards, "w")
screen.onkeypress(move_backwards, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear_screen, "c")



screen.exitonclick()