MANU = {
    "espresso": {
        "ingredient":{
            "water": 50,
                "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredient": {
            "water": 200,
            "milk": 150,
            "coffee": 24
            
        },
        "cost": 2.5 
    },
    
    "cappuccino":{
        "ingredient": {
            "water": 250,
            "milk": 100,
            "coffee": 24
            
        },
        "cost": 3.0 
    }
}

profit = 0
resources = {
    "water":300,
    "milk":200,
    "coffee":100
}



def is_resource_sufficient(order_integredient):
    """Return True when order can be made, False if integredients are insuffisient."""
    for item in order_integredient:
       if order_integredient[item] >= resources[item]:
           print(f"Sorry there is enough {item}")
           return False
    return True


def process_coin():
    """Return total calculated from coins inserted."""
    print("please insert coins")
    total = int(input("How many quater? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickle? ")) * 0.05
    total += int(input("How many pennie? ")) * 0.01
    return total


def is_transaction_successfull(money_recive, drink_cost):
    if money_recive >= drink_cost:
        change = round(money_recive - drink_cost, 2)
        print(f"Here is your change {change}$")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that enough money, Money refunded.")
        return False
    

def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name} ☕ Enjoy! ")


is_on = True
while is_on:
   choice = input("What would you like? (espresso/Latte/cappuccino): ")
   if choice == "off":
      is_on = False
   elif choice == "report":
      print(f"water: {resources['water']}ml")
      print(f"Milk: {resources['milk']}ml")
      print(f"Coffee: {resources['coffee']}g")
      print(f"Money: {profit}$")
   else:
       drink = MANU[choice]
       if is_resource_sufficient(drink["ingredient"]):
           payment = process_coin()
           if is_transaction_successfull(payment, drink['cost']):
               make_coffee(choice, drink['ingredient'])