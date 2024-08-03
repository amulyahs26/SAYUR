'''Write a program to calculate the milege. Ask the user how many litres of petrol they have.
Ask how many km they have to drive. Calcualte the milege. If the mileage is more than 30km per litre, tell 
the user they have to fill the tank again.'''

while True:
    petrol=float(input("How many liter petrol you have in tank: "))
    if petrol<=0 or petrol>10000:
        print("Enter valid liters!!")
    else:
        break

while True:
    distance=float(input("Enter the distance you want to travel:"))
    if distance<=0:
        print("Enter valid distance!!")
    else:
        break

def milege(distance,petrol):
    milege=distance/petrol
    if milege>30:
        print("You have to fill the tank again!!")
    else:
        print("Happy journey")

milege(distance,petrol)
