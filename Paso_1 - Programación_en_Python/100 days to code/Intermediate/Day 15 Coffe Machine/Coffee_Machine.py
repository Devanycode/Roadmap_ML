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
    "money": 0
}

def off_machine():
    """Con esta función se finaliza el proceso de la máquina de café"""
    return

def report():
    """Informa la cantidad de recursos que hay actualmente en la máquina"""
    print(f"Water: {resources["water"]}ml\n"
          f"Milk: {resources["milk"]}\n"
          f"Coffee: {resources["coffee"]}\n"
          f"Money: {resources["money"]}")

def sufficient_resources(drink):
    """Comprueba si hay recursos suficientes """
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def start_machine():
    """Imprime los precios y pide al usuario que bebida desea
    También se puede pedir el reporte o apagar la máquina de café desde aquí"""
    prices = (f"Espresso: ${MENU["espresso"]["cost"]}\n"
              f"Latte: ${MENU["latte"]["cost"]}\n"
              f"cappuccino: ${MENU["cappuccino"]["cost"]}")
    while True:
        print("\n")
        print(prices)
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_choice in ["espresso", "latte", "cappuccino"]:
            available_drink = sufficient_resources(coffee_choice)
            if available_drink:
                insert_coins(coffee_choice)
        elif coffee_choice == "report":
            report()
        elif coffee_choice == "off":
            off_machine()
            return
        else:
            print("Please, Type a valid drink.")

def insert_coins(drink):
    print("Please, insert coins.")
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            enough_money(money = total_money, drink = drink)
            return
        except ValueError:
            print("Please, input a number. Try again.")

def enough_money(money, drink):
    """Se comprueba si el dinero ingresado por el usuario es suficiente
    para la bebida solicitada"""
    if money > MENU[drink]["cost"]:
        print(f"Here is ${money - MENU[drink]["cost"]:.2f} dollars in change.")
        print(f"Here is your {drink}. Enjoy!☕")
        resources["money"] = resources["money"] + money
        for item in MENU[drink]["ingredients"]:
            resources[item] -= MENU[drink]["ingredients"][item]
        return
    elif money == MENU[drink]["cost"]:
        print(f"Here is your {drink}. Enjoy!☕")
        resources["money"] += money
        return
    else:
        print("The amount entered is not enough, please try again."
              f"We reimburse you ${money}")
        return


start_machine()

