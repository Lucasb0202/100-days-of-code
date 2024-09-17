from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
  choice = input("What would you like? (espresso/latte/cappuccino): ")
  if choice == "report":
    coffee_machine.report()
    money_machine.report()
  elif choice == "off":
    break
  else:
    drink = menu.find_drink(choice)
    if choice in menu.get_items():
      if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_machine.make_coffee(drink)