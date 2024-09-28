from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.level = 0
    self.penup()
    self.hideturtle()
    self.update_scoreboard()

  def update_scoreboard(self):
    self.goto(-280, 260)
    self.clear()
    self.write(f"Level: {self.level}", move=False , align='left', font=FONT)
    
  def increase_level(self):
    self.level += 1
    self.update_scoreboard()
