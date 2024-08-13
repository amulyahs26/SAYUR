'''Same as vegetable_store.py problem . You also need list all the sales by customer in a day and  print what is the
max amount of sale.
'''
# Dictionary to maintain food name, price per 100 grams, and quantity available
vegetables = {
    'tomato': {'price_per100gms': 10, 'quantity': 5 * 1000},  # Quantity in grams
    'capsicum': {'price_per100gms': 15, 'quantity': 3 * 1000},
    'brinjal': {'price_per100gms': 20, 'quantity': 4 * 1000},
    'onion': {'price_per100gms': 25, 'quantity': 6 * 1000},
    'potato': {'price_per100gms': 10, 'quantity': 7 * 1000},
    'carrot': {'price_per100gms': 15, 'quantity': 5 * 1000}
}

# List to keep track of all sales for the day
sales = []

def print_inventory():
    for item, details in vegetables.items():
        quantity = details['quantity']
        if quantity >= 1000:
            print(f"{quantity / 1000} kg {item.capitalize()} is available")
        else:
            print(f"{quantity} gms {item.capitalize()} is available")

def update_inventory(item, amount, units):
    if units == 'kg':
        amount_grams = amount * 1000
    else:  # units == 'grams'
        amount_grams = amount

    if item in vegetables:
        if vegetables[item]['quantity'] >= amount_grams:
            vegetables[item]['quantity'] -= amount_grams
            return True
        else:
            print(f"Not enough {item} available. Only {vegetables[item]['quantity']} grams left.")
            return False
    else:
        print(f"{item} is not available in the store.")
        return False

def add_sale(item, amount, units, cost):
    sales.append({
        'item': item,
        'amount': amount,
        'units': units,
        'cost': cost
    })

def print_sales():
    print("Sales for the day:")
    for sale in sales:
        item = sale['item'].capitalize()
        amount = sale['amount']
        units = sale['units']
        cost = sale['cost']
        print(f"{amount} {units} of {item} for {cost} INR")

# To store the total cost
total_cost = 0

while True:
    # Get user input
    item_input = input("Enter the item you want to buy in the format 'food:amount units' (e.g., tomato:2 kg): ").strip().lower()

    if item_input == "that's it":
        break

    # Parse the input
    try:
        food_item, rest = item_input.split(':')  # Split the input on the colon
        amount, units = rest.split()  # Split the rest on the space to get amount and units
        amount = float(amount)
    except ValueError:
        print("Please enter the input in the correct format: Food:amount units")
        continue  # Ask for the input again if the format is incorrect

    # Validate units
    if units not in ['kg', 'grams']:
        print("Please enter a valid unit (either 'kg' or 'grams').")
        continue  # Ask for input again

    # Validate food item and amount
    if not update_inventory(food_item, amount, units):
        continue

    # Calculate cost
    if units == 'kg':
        cost = (amount * 1000 / 100) * vegetables[food_item]['price_per100gms']  # Convert kg to grams
    else:  # units == 'grams'
        cost = (amount / 100) * vegetables[food_item]['price_per100gms']

    # Add to total cost
    total_cost += cost
    add_sale(food_item, amount, units, cost)
    print(f"Added {amount} {units} of {food_item} for {cost} INR to your cart.")

    # Prompt for next action
    while True:
        next_action = input("Do you want to 1) add another item or 2) finish? (Enter 1 or 2): ").strip()
        if next_action == '1':
            break  # Exit the inner loop to add another item
        elif next_action == '2':
            # Exit both loops to finish and display the total cost
            print(f"Your total cost is {total_cost} INR.")
            print_inventory()  # Print the inventory at the end of the sale
            print_sales()  # Print all sales for the day
            if sales:
                max_sale = max(sale['cost'] for sale in sales)
                print(f"The maximum sale amount for today is {max_sale} INR.")
            else:
                print("No sales were made today.")
            exit()  # Exit the program
        else:
            print("Please enter a valid option (1 or 2).")
