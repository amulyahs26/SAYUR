'''Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or mininum.
Find the answer and print.'''

# Ask the user to input 3 numbers
num1 = int(input("Enter the num1:"))
num2 = int(input("Enter the num2:"))
num3 = int(input("Enter the num3:"))

# Ask the user if they want to find the max or min of these numbers
while True:
    find = input("Enter 'max' or 'min' to find the maximum or minimum: ").strip().lower()
    if find not in ['max', 'min']:
        print("Please enter a valid choice (max or min)!!")
    else:
        break

# Function to find the max or min
def func(num1, num2, num3, find):
    if find == 'max':
        result = max(num1, num2, num3)
    else:
        result = min(num1, num2, num3)
    return result

# Find the result and print
result = func(num1, num2, num3, find)
print(f"The {find} of the numbers is: {result}")

    
