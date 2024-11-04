#lambda with sort

sorted_numbers=sorted([1,5,3,4,2])
print(sorted_numbers)

siblings=[
    {'name':'amulya','age':21},
    {'name':'surabhi','age':25},
    {'name':'shravanth','age':15},
    {'name':'kushal','age':12}
]

sorted_siblings=sorted(siblings,key=lambda siblings:siblings['age'])
print(sorted_siblings)