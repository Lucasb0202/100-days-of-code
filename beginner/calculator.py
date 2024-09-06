def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

first_num = float(input("Whats the first number?: "))

while True:
  operation = input("Pick an operation: ")
  next_num = float(input("Whats the next number?: "))

  result = operations[operation](first_num, next_num)
  print(f"{first_num} {operation} {next_num} = {result}")

  continue_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
  if continue_calculating == "n":
    break
  else: 
    first_num = result
  