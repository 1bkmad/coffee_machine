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

coins = {
    "penny": 0.01,
    "dime": 0.10,
    "nickel": 0.05,
    "quarter": 0.25
}

Money = 0.0
switch = 'True'


# TODO 2) machine should be able to print resources/report left every time.


def report():
    # report function to print report
    for i in resources.keys():
        if i == "coffee":
            print(f"{i}: {resources[i]}mg")
        else:
            print(f"{i}: {resources[i]}ml")
    print(f"Money: ${Money}")


# TODO 3) Always should check if resources are available for particular drink or not.
def resources_check(drink):
    # Function to check if enough resources are available for coffee or not.
    for i in resources.keys():
        if i in MENU[drink]["ingredients"]:
            if resources[i] < MENU[drink]["ingredients"][i]:
                print(f"Sorry, Not enough {i} left in machine")
                return False
        else:
            continue
        return True


'''
 TODO 4) After user gives the type of drink he wants, ask for money and user will give input of 
  coins (ask coins in format of penny:, nickel: dime: etc, i.e. ask user to insert number of specific coins each time.)
  If recieved more than required, return the change left. And print the msg to enjoy the coffee.
  If money not enough then return the changes.
'''


def money(drink):
    # function to calculate total money paid by user as well as left over change.
    print("Please insert coins")
    total_money = round(0, 2)
    for i in coins.keys():
        count = int(input(f"How many {i} "))
        total_money += count * coins[i]
    left_money = round(total_money - MENU[drink]["cost"], 2)
    return left_money


# TODO 5) In report, these transaction changes should be mentioned.
def left_resources(drink):
    # function to calculate leftover resources
    for i in resources.keys():
        if i in MENU[drink]["ingredients"]:
            resources[i] -= MENU[drink]["ingredients"][i]


while switch:
    # TODO 1) Ask the user what do they want : espresso/latte/cappuccino or report of left over items in machine
    correct_responses = ["espresso", "latte", "cappuccino", "off", "report"]
    want = input(print("What would you like? (espresso/latte/cappuccino) ")).lower()
    if want not in correct_responses:
        print("Please enter valid choice ")
        for i in range(0, 3):
            print(f"type '{correct_responses[i]}' for {correct_responses[i]} ")
        print("type 'off' for turning the machine off ")
        print("type 'report' for resources left in machine ")
    else:
        if want == "report":
            report()
        elif want == "off":
            switch = False
        else:
            if resources_check(want):
                return_money = money(want)
                if return_money < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    if return_money > 0:
                        print(f"Here's your ${round(return_money, 2)} change")
                    print(f"Here is your {want}  enjoy!!")
                Money += MENU[want]["cost"]
                left_resources(want)
