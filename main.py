money = 0
insert_coin = 0.0
continue_running = False

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def display(dictionary):
    print(f"water:  {dictionary['water']}ml")
    print(f"milk:   {dictionary['milk']}ml")
    print(f"coffee: {dictionary['coffee']}g")
    print(f"money:  ${money}")


def check_resource(order):

    if resources['water'] < MENU[order]['ingredients']['water']:
        return 1
    elif response != "espresso" and resources['milk'] < MENU[order]['ingredients']['milk']:
        return 2
    elif resources['coffee'] < MENU[order]['ingredients']['coffee']:
        return 3
    else:
        return 0


def check_coin(order):

    global money, insert_coin
    print("insert coin")
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles?: ")) * 0.05
    pennies = float(input("how many pennies: ")) * 0.01
    insert_coin = quarters + dimes + nickles + pennies

    if MENU[order]["cost"] > insert_coin:
        print(f"Sorry you dont have enough money, {insert_coin} refunded")
    else:
        money += MENU[response]['cost']
        return 0


def operate():
    global continue_running
    if response == "report":
        print(display(resources))
    elif response == "latte" or response == "cappuccino" or response == "espresso":
        storage = check_resource(response)
        if storage == 1:
            print("sorry there is not enough water")
        elif storage == 2:
            print("sorry there is not enough milk")
        elif storage == 3:
            print("sorry there is not enough coffee")
        elif storage == 0:
            enough_coin = check_coin(response)
            if enough_coin == 0 and response == "latte" or response == "cappuccino":
                resources['water'] = resources['water'] - MENU[response]['ingredients']['water']
                resources['milk'] = resources['milk'] - MENU[response]['ingredients']['milk']
                resources['coffee'] = resources['coffee'] - MENU[response]['ingredients']['coffee']
                print(f"Here is $ {round (insert_coin - MENU [response]['cost'], 2)} in change")
                print(f"Here is your {response}, Enjoy!!")
            elif enough_coin == 0 and response == "espresso":
                resources['water'] = resources['water'] - MENU[response]['ingredients']['water']
                resources['coffee'] = resources['coffee'] - MENU[response]['ingredients']['coffee']
                print(f"Here is $ {round(insert_coin - MENU[response]['cost'], 2)} in change")
                print(f"Here is your {response}, Enjoy!!")
    elif response == "off":
        continue_running = True


while not continue_running:

    response = input("What would you like? (espresso/latte/cappuccino): ").lower()
    operate()




