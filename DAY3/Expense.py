'''Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per
 person is half of lunch cost. Cost of the hall is Rs 200 per person.
  Decoration is 50% of Hall cost. Parking is 10% of the Hall cost. 
  Decide what should be the input and calculate the cost.'''

'''Start with the above. The total cost is split equally by bride and groom.
 Bride has saved Rs50000. Determine if the bride has to take a loan or not. 
 If loan, how much?'''

while True:
    no_persons=int(input("Enter the number persons coming to wedding:"))
    if no_persons<=0:
        print("Please enter valid number!!")
    else:
        break
    
cost_lunch=200
cost_hall=200
cost_breakfast=cost_lunch/2
decoration_cost=cost_hall*0.5
parking_cost=cost_hall*0.1
total_cost=no_persons*(cost_hall+cost_breakfast+cost_lunch+decoration_cost+parking_cost)
#based on the total_cost we can say the input budget

print(f"The total_cost of a wedding is {total_cost}")
print(f"The input budget should be >= {total_cost}")

bride_shared=total_cost/2
print(f"bride shared amount is {bride_shared}")
bride_saved=50000
def loan_amt(bride_saved,bride_shared):
   loan=bride_shared-bride_saved
   if bride_saved<=bride_shared:
      print(f"Bride has to take loan!!,Loan price is {loan}")
   else:
       print("Bride doesnot have to loan!!")
  
loan_amt(bride_saved,bride_shared)
