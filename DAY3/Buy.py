'''7.Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget. 
7.1 Same as above, but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city.
7.2 Same as above, but add 3% of the budget for petrol expenses. '''

while True:
    budget=int(input("Enter the budget you have: "))
    if budget<=0:
        print("You cannot buy any item with this budget!!")
    else:
        break
petrol_expense=budget*0.03
remaining_budget=budget-petrol_expense

city_price={'chennai':30,'trichy':27,'madurai':34}

while True:
    city=input("Enter the city name:").strip().lower()
    if city not in city_price:
        print("please enter valid city name:")
    else:
        break
    
def onion_price(city,city_price):
    if city in city_price:
        return city_price[city]
    else:
        None

onion_city_price=onion_price(city,city_price)
number_of_onion=int(remaining_budget/onion_city_price)
number_of_tomato=int(remaining_budget/10.5)
print(f"Number of onion you can buy with this amount is {number_of_onion}")
print(f"Number of onion you can buy with this amount is {number_of_tomato}")


