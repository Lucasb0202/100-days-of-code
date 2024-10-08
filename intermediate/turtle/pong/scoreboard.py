from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update_scoreboard()

  def update_scoreboard(self):
    self.goto(-100, 200)
    self.write(f"{self.l_score}", move=False, align='right', font=FONT)
    self.goto(100, 200)
    self.write(f"{self.r_score}", move=False, align='left', font=FONT)

  def increment_left(self):
    self.l_score += 1
    self.clear()
    self.update_scoreboard()
  
  def increment_right(self):
    self.r_score += 1
    self.clear()
    self.update_scoreboard()
