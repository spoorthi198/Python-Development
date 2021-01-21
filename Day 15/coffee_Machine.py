MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def report():
    water = resources["water"]

    milk = resources["milk"]

    coffee = resources["coffee"]

    return f"water:{water}," \
           f"milk:{milk}," \
           f"coffee:{coffee}," \




def calculate_money():
    total=int(input("insert coin in quarters"))*0.25
    total += int(input("insert coin in dimes")) * 0.10
    total += int(input("insert coin in nickles")) * 0.05
    total += int(input("insert coin in pennies")) * 0.01
    return total



def is_resource_sufficient(order):
    for item in order:
        if order[item]>resources[item]:
            print(f"sorry not enough resources{item}")
            return False
        else:
            return True



def transaction_successful(money_received,drink_cost):
    """ this func return true if transaction success false when it is not"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"sorry not enough money ${money_received} refunded")
        return False

def make_coffee(drink_name,order):
    for item in order:
        resources[item]-=order[item]
    print(f"enjoy your {drink_name}coffee")






is_on = True

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino/report):?\n").lower()

    if user_input == 'off':
        is_on = False
    elif user_input == 'report':
        print(f"report is: {report()}")
    else:
        drink = MENU[user_input]
        order_items = drink["ingredients"]
        if is_resource_sufficient(order_items):
            print("resource available")
            payment=calculate_money()
            print(payment)
            transaction_successful(payment,drink["cost"])
            make_coffee(user_input,order_items)
        else:
            print("Sorry there is not enough resource.")










