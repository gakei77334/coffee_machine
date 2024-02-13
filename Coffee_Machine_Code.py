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


def display_report():
    """Display current resources"""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")
    

def insert_coins():
    global total_coins
    """Prompt user to insert coins and calculate the total they've put in""" 
    quarters = int(input("How many quarters?: " )) * 0.25 
    dimes = int(input("How many dimes?:" )) * 0.10
    nickels = int(input("How many nickels?:" )) * 0.05
    pennies = int(input("How many pennies?:" )) * 0.01
    
    total_coins = quarters + dimes + nickels + pennies
    
    return total_coins


def deduct_resources(coffee):
    """Deduct resources based on coffee selection"""
    if coffee == 'espresso':
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
        
    elif coffee == 'latte' or coffee == 'cappuccino':
        resources['water'] -= MENU[coffee]['ingredients']['water']
        resources['milk'] -= MENU[coffee]['ingredients']['milk'] 
        resources['coffee'] -= MENU[coffee]['ingredients']['coffee']

           
def check_resources(coffee):
    # Check if coffee selected is in the MENU
    if coffee in MENU:
        required_ingredients = MENU[coffee]['ingredients'] # If YES get the required ingredients
        for ingredient in required_ingredients: # Iterate through each ingredient
            amount_required = required_ingredients[ingredient] # Get the amount of the CURRENT ingredient required
            if amount_required > resources[ingredient]: # Check if the available amount of the ingredient is < required
                print(f"Sorry, not enough {ingredient}")
                return False
            else:
                return True
            
            
def process_payment(coffee, total_coins):
    global change
    drink_cost = MENU[coffee]['cost']    
     
    if total_coins < drink_cost:
        return False
    
    # The True part, enough coins for cost of drink
    if total_coins >= drink_cost:
        change = round(total_coins - drink_cost,2) # Round to 2 d.p
        resources['money'] += drink_cost
        return change
    else:        
        print("Sorry, not enough money")
        return total_coins # If the payment is not enough, return the total coins
    
##### Running Machine #####

power_on = True

while power_on is True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if coffee == 'off': # If user wants to turn off the machine
        print("Shut down")
        power_on = False # Exit the loop
    elif coffee == 'report': # If user wants to see report
        display_report()
    else: # If user wants to order a drink
        if check_resources(coffee) is True: # Check if there are enough resources to order a drink. If yes then True
            insert_coins()
            
            # Check if payment is True and not False (enough coins for cost of drink)
            if process_payment(coffee, total_coins) is not False:
                if change >= 0: # If payment is more than cost of drink
                    deduct_resources(coffee)
                    print(f"Here's your change: £{change}")
                    print(f"Here's your drink: {coffee}")
            else:
                print(f"Money refunded: {total_coins}")
                
##### End of running machine #####
