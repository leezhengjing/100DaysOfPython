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
    "money": 0,
}


# Function that checks the choice of the user.
def check_choice(choice):
    if choice == 'off':
        return False
    elif choice == 'report':
        report()
        return False
    else:
        return True


# Function that prints a report of current resources
def report():
    for resource in resources:
        if resource == 'coffee':
            print(f"{resource.title()}: {resources[resource]}g")
        elif resource == 'money':
            print(f"{resource.title()}: ${resources[resource]}0")
        else:
            print(f"{resource.title()}: {resources[resource]}ml")


# Function that checks if there is sufficient resources to make the drink of choice
def check_resources(choice_resources):
    if choice_resources['water'] > resources['water']:
        return False
    if choice_resources['coffee'] > resources['coffee']:
        return False
    try:
        if choice_resources['milk'] > resources['milk']:
            return False
    except KeyError:
        return True
    else:
        return True


# Function that processes coins
def process_coins(coins_value):
    total_money = 0
    for key in coins_value:
        coins_quantity = int(input(f"How many {key}?: "))
        total_money += coins_value[key] * coins_quantity
    return total_money


# Function that checks if transaction is successful.
def check_transaction(choice_cost, total_money):
    if choice_cost <= total_money:
        return True
    else:
        print("Sorry, thats not enough money. Money refunded.")
        return False


# Function that updates the resources remaining in the coffee machine.
def update_resources(choice_resources):
    for resource in choice_resources:
        resources[resource] -= choice_resources[resource]


def check_lacking_resource(choice_resources):
    lacking_resources = ''
    for resource in choice_resources:
        if choice_resources[resource] > resources[resource]:
            lacking_resources += f'\n{resource.card_title()}'
    return lacking_resources


# Main program function
def coffee_machine():
    is_running = True
    while is_running:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == 'off':
            is_running = False
        elif choice == 'report':
            report()
            continue
        else:
            choice_drink = MENU[choice]
            choice_resources = choice_drink['ingredients']
            choice_cost = choice_drink['cost']
            is_sufficient_resources = check_resources(choice_resources)
            if is_sufficient_resources:
                coins_value = {
                    'quarters': 0.25,
                    'dimes': 0.10,
                    'nickels': 0.05,
                    'pennies': 0.01,
                }
                print("Please insert coins.")
                total_money = process_coins(coins_value)
                is_successful_transaction = check_transaction(choice_cost, total_money)
                if is_successful_transaction:
                    resources['money'] += choice_cost
                    change = total_money - choice_cost
                    print(f"Here is ${change}0 in change.")
                    print(f"Here is your ☕{choice}. Enjoy!")
                    update_resources(choice_resources)



            else:
                lacking_resources = check_lacking_resource(choice_resources)
                print(f'Sorry there is not enough: {lacking_resources}')
                continue


coffee_machine()
