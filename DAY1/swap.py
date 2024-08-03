'''Write a program that will swap two numbers.'''

while True:
    try:
        num1=int(input("Enter the num1 value:"))
        num2=int(input("Enter the num2 value:"))
        break
    except ValueError:
        print("Please enter the valid numbers!!")

    
def swap_func(num1,num2):
    return num2,num1

#call the swap function    
num1, num2 = swap_func(num1, num2)

# Print the swapped numbers
print(f"After swapping: num1 = {num1}, num2 = {num2}")
