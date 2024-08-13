'''Write a program for a  vegetable store.
Create a dictionary to maintain the food name and price per 100 grams.
Input from the user will be in the format Food:amount units
(for eg Tomato:2 Kg 
or Tomato: 200 gms). User will give many input. When the user input is 'That's it', 
find the total cost. '''

vegetables_per100gms={'tomato':10,'capsicum':15,'brinjal':20,'onion':25,'potato':10,'carrot':15}
total_cost=0
while True:
    item=input("Enter the item you want to buy in the formate food:amount per units =").strip().lower()
    
    try:
        item,rest=item.split(':')# Split the input on the colon to separate the food item and the rest of the input
        amount,units=rest.split()# Split the rest on the space to separate the amount and the units
        amount=float(amount)
    except ValueError:
        print("Please enter the input in the correct format:'food:amount units' (e.g., tomato:2 kg): ")
        continue # Ask for the input again if the format is incorrect
    
    if units not in ['kg', 'grams']:
        print("Please enter a valid unit (either 'kg' or 'grams').")
        continue  # Ask for input again

    if item not in vegetables_per100gms or amount<=0:
        print("Either Item is out of stock!! or amount you enter is invalid please check once!!")
        continue

    if units == 'kg':
        cost = (amount * 1000 / 100) * vegetables_per100gms[item]  # Convert kg to grams
    else:  # units == 'grams'
        cost = (amount / 100) * vegetables_per100gms[item]

    # Add to total cost
    total_cost += cost
    print(f"Added {amount} {units} of {item} for {cost} INR to your cart.")

    while True:
        ask= input("Do you want to 1) add another item or 2)That's it (Enter 1 or 2): ").strip()
        if ask == '1':
            break  # Exit the inner loop to add another item
        elif ask == '2':
            # Exit both loops to finish and display the total cost
            print(f"Your total cost is {total_cost} INR.")
            exit()  # Exit the program
        else:
            print("Please enter a valid option (1 or 2).")



