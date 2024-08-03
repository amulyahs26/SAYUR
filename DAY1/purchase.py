'''The user just bought a few things in your  shop. Ask the user what he bought.
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype'''

while True:
    vadai=int(input("Enter the number of vadai purchased:")) #validate item 
    if vadai<0:
        print("Enter the valid number!!!")
    else:
        break

while True:
    soda=int(input("Enter the number of soda purchased:")) #validate item
    if soda<0:
        print("Enter the valid number!!!")
    else:
        break
while True:
    sandwich=int(input("Enter the number of sandwich purchased:")) #validate item
    if sandwich<0:
        print("Enter the valid number!!!")
    else: 
        break

total_cost=vadai*30+soda*20+sandwich*100  #calc total cost 
print(f"Total cost you should pay is {total_cost}Rs")
while True:
    paid_amt=float(input("Enter the paid amount:"))  #get validate paid amount
    if paid_amt<0 or paid_amt<total_cost:
        print("Please pay valid amount!!!")
    else:
        break
change=paid_amt-total_cost
print(f"Your change is {change} rupees")
