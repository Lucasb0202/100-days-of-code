def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
      if year % 100 == 0 and year % 400 == 0:
        return True
      elif year % 100 == 0:
        return False
      else: return True
    else: return False

is_leap_year(2100)

def fizz_buzz(target):
  for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
    elif number % 3 == 0:
      print("Fizz")
    elif number % 5 == 0:
      print("Buzz")
    else:
      print(f"[{number}]")

fizz_buzz(15)