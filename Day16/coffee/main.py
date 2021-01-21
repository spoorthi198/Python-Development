from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




cofee_maker=CoffeeMaker()

menu = Menu()
money_machine=MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"please chose the order{options} \n")
    if choice == "report":
        cofee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):

            cofee_maker.make_coffee(drink)


