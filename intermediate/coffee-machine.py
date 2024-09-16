MENU = {
  "espresso": {
      "ingredients": {
          "water": 50,
          "milk": 0,
          "coffee": 18,
      },
      "cost": 1.5,
  },
  "latte": {
      "ingredients": {
          "water": 200,
          "milk": 150,
          "coffee": 24,
      },
      "cost": 2.5,
  },
  "cappuccino": {
      "ingredients": {
          "water": 250,
          "milk": 100,
          "coffee": 24,
      },
      "cost": 3.0,
  }
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}

def check_avaliability():
  for key in resources:
    if resources[key] < MENU[choice]["ingredients"][key]:
      print(f"Sorry there is not enough {key}.")
      return False
  return True

def show_report(money):  
  for key in resources:
    if key == "water" or key == "milk":
      print(key.title() + ": " + str(resources[key]) + "ml")
    else: print(key.title() + ": " + str(resources[key]) + "g")
  print(f"Money: ${money}")
  
def calculate_total():
  quarters = float(input("How many quarters?: "))
  dimes = float(input("How many dimes?: "))
  nickles = float(input("How many nickles?: "))
  pennies = float(input("How many pennies?: "))

  return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

money = 0.0
while True:
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice.lower() == "off":
    break
  elif choice.lower() == "espresso" or choice.lower() == "latte" or choice.lower() == "cappuccino":
    if check_avaliability():
      print("Please insert coins.")
      total = calculate_total()
      if total < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
      else:
        for key in resources:
          resources[key] -= MENU[choice]["ingredients"][key]
        money += MENU[choice]["cost"]
        print(f"Here is ${round(total - MENU[choice]["cost"], 2)} in change.")
        print(f"Here is your {choice} ☕ Enjoy!")
  elif choice.lower() == "report":
    show_report(money)
  else: print("Enter a valid coffee option.")
