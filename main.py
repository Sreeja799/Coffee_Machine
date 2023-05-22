from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
machine = MoneyMachine()

while True:
    prompt = input(f"What would you like? ({menu.get_items()}): ")
    if prompt == 'off':
        break
    elif prompt == 'report':
        coffee.report()
        machine.report()
    else:
        order = menu.find_drink(prompt)
        if order:
            if coffee.is_resource_sufficient(order):
                if machine.make_payment(order.cost):
                    coffee.make_coffee(order)