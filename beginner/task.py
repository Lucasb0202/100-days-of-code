def is_prime(num):
  count = 0
  for i in range(1, num + 1):
    if num % i == 0:
      count += 1
  return count == 2

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
