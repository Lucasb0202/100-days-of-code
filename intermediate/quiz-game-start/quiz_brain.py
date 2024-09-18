class QuizBrain:
  def __init__(self, questions_list):
    self.question_number = 0
    self.questions_list = questions_list
    self.score = 0
  
  def next_question(self):
    answer = input(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].question} (True/False)?: ")
    self.check_answer(answer)
    self.question_number += 1
  
  def still_has_questions(self):
    return self.question_number < len(self.questions_list)
  
  def check_answer(self, answer):
    if answer.lower() == self.questions_list[self.question_number].correct_answer.lower():
      self.score += 1
      print("You got it right!")
    else:
      print("You got it wrong!")
    print(f"The correct answer was: {self.questions_list[self.question_number].correct_answer}.")
    print(f"Your current score is: {self.score}/{self.question_number + 1}.")
    print("\n")